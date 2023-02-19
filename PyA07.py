from bs4 import BeautifulSoup
import requests


def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        # write your ✨magical✨ code here
        results = []
        jobs = soup.find_all("tr", class_="job")
        for job in jobs:
            tmp = job.find(class_="company position company_and_position")
            job_data = {
                "title": tmp.find(itemprop="title").string.strip(),
                "name": tmp.find(itemprop="name").string.strip(),
                "location": tmp.find(class_="location").string.strip(),
            }
            results.append(job_data)
        for result in results:
            print(result)
    else:
        print("Can't get jobs.")


extract_jobs("rust")
# extract_jobs("golang")
# extract_jobs("python")
