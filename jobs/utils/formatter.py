def normalize_jobs(jobs):
    normalized = []

    for job in jobs:
        normalized.append({
            "Job_Title": job.get("job_title", "N/A"),
            "Company_Name": job.get("company", "N/A"),
            "Location": job.get("location", "N/A"),
            "Experience_Required": job.get("experience", "N/A"),
            "Salary": job.get("salary", "N/A"),
            "Job_Portal": job.get("portal", "N/A"),
            "Job_URL": job.get("url", "#")
        })

    return normalized
