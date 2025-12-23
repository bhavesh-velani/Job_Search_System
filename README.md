** Job Vacancy Search System (Django + Web Scraping) **

1.Project Overview
-->This project allows users to search job vacancies using designation, location, and experience level.
-->Job listings are scraped from multiple job portals and displayed in a unified format.

2.Job Portals Used
-->Jobsora India (https://in.jobsora.com)
-->Naukri.com (https://www.naukri.com)

3.Technology Used
-->Python
-->Django
-->BeautifulSoup
-->Requests
-->Selenium (fallback)
-->JSON

4.Features
-->Dynamic search URL generation
-->Pagination handling
-->Logging for debugging
-->Safe scraping with error handling
-->JSON output generation

5.Output
-->Job listings displayed on UI
-->Exported to `output/jobs.json` and `output/jobs.xlxx`

6.Challenges Faced
-->Handling missing HTML elements
-->Pagination detection

7.Solution
-->Added pagination loop
-->Provided Selenium fallback

8.How to Run
-->Install dependencies
-->Run Django server
-->Enter job details and search

