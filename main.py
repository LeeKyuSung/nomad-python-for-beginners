from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("status_code : " + response.status_code)
else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("section", class_="jobs")
    for job_section in jobs:
        job_posts = job_section.find_all("li")
        job_posts.pop()
        for post in job_posts:
            anchors = post.find_all("a")
            anchor = anchors[1]
            company, kind, region = anchor.find_all("span", class_="company")
            title = anchor.find("span", class_="title")
            job_data = {
                'title': title.string,
                'company': company.string,
                'region': region.string,
                'position': title.string
            }
            results.append(job_data)
    for result in results:
        print(result)
