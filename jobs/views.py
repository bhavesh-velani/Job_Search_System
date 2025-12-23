from django.shortcuts import render
from .forms import JobSearchForm
from .scraper.jobsora_scraper import scrape_jobsora
from .scraper.naukari_selenium import scrape_naukri_selenium
from .utils.formatter import normalize_jobs
import json
import os
import pandas as pd

def job_search(request):
    form = JobSearchForm()
    jobs = []

    if request.method == "POST":
        form = JobSearchForm(request.POST)
        if form.is_valid():
            designation = form.cleaned_data["designation"]
            location = form.cleaned_data["location"]
            experience = form.cleaned_data["experience"]

            jobsora_jobs = scrape_jobsora(designation, location, experience)
            naukri_jobs = scrape_naukri_selenium(designation, location, experience)

            all_jobs = jobsora_jobs+naukri_jobs
            jobs = normalize_jobs(all_jobs)

            os.makedirs("output", exist_ok=True)
            
            with open("output/jobs.json", "w", encoding="utf-8") as f:
                json.dump(jobs, f, indent=4)
                
            df = pd.DataFrame(jobs)
            df.to_csv("output/jobs.xlsx", index=False, encoding="utf-8-sig")

    return render(request, "results.html", {"form": form, "jobs": jobs})
