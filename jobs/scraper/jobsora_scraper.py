import re
import requests
from bs4 import BeautifulSoup

def scrape_jobsora(designation, location, experience, max_pages=3):
    designation = designation.replace(" ", "-")
    location = location.replace(" ", "-")

    base_url = f"https://in.jobsora.com/jobs?query={designation}&location={location}&extra={experience}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    exp_map = {
        0: "Fresher",
        1: "1-3 Years",
        2: "3-5 Years"
    }

    jobs = []

    for page in range(1, max_pages + 1):
        url = base_url if page == 1 else f"{base_url}&page={page}"
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        cards = soup.find_all("article")
        if not cards:
            break

        for card in cards:
            title_tag = card.find("h2", class_="c-job-item__title")
            job_title = title_tag.text.strip() if title_tag else "N/A"
            job_url = title_tag.find("a")["href"] if title_tag and title_tag.find("a") else "#"

            info = card.find_all("div", class_="c-job-item__info-item")
            company = info[0].text.strip() if len(info) > 0 else "Not Mentioned"
            job_location = info[1].text.strip() if len(info) > 1 else "Not Mentioned"

            desc = card.find("p", class_="c-job-item__description")
            text = desc.text if desc else ""

            exp_match = re.search(r"Experience\s*:\s*([\d\+\-\s]+years?)", text, re.I)
            exp = exp_match.group(1) if exp_match else exp_map.get(experience, "Not Mentioned")

            sal_match = re.search(r"([\d\.]+\s*LPA\s*[-\-]\s*[\d\.]+\s*LPA)", text)
            salary = sal_match.group(1) if sal_match else "Not Disclosed"

            jobs.append({
                "job_title": job_title,
                "company": company,
                "location": job_location,
                "experience": exp,
                "salary": salary,
                "portal": "Jobsora",
                "url": job_url
            })

    return jobs