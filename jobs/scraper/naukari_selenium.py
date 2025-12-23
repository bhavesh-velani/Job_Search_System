import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def scrape_naukri_selenium(designation, location, experience, max_pages=2):
    designation = designation.replace(" ", "-")
    location = location.replace(" ", "-")

    base_url = f"https://www.naukri.com/{designation}-jobs-in-{location}?experience={experience}"

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    jobs = []

    for page in range(1, max_pages + 1):
        url = base_url if page == 1 else f"{base_url}&pageNo={page}"
        driver.get(url)
        time.sleep(5)

        cards = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")
        if not cards:
            break

        for card in cards:
            try:
                title = card.find_element(By.CLASS_NAME, "title")
                company = card.find_element(By.CLASS_NAME, "comp-name")
                exp = card.find_element(By.CLASS_NAME, "expwdth")
                loc = card.find_element(By.CLASS_NAME, "locWdth")

                try:
                    salary = card.find_element(By.CLASS_NAME, "sal").text
                except:
                    salary = "Not Disclosed"

                jobs.append({
                    "job_title": title.text.strip(),
                    "company": company.text.strip(),
                    "location": loc.text.strip(),
                    "experience": exp.text.strip(),
                    "salary": salary,
                    "portal": "Naukri",
                    "url": title.get_attribute("href")
                })
            except:
                continue

    driver.quit()
    return jobs
