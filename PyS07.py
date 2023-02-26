from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, request, redirect


def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("tr", class_="job")
        for job in jobs:
            company = job.find("h3", itemprop="name")
            position = job.find("h2", itemprop="title")
            location = job.find("div", class_="location")
            if company:
                company = company.string.strip()
            if position:
                position = position.string.strip()
            if location:
                location = location.string.strip()
            if company and position and location:
                job = {
                    "company": company,
                    "position": position,
                    "location": location,
                }
                results.append(job)
    else:
        print("Can't get jobs.")
    return results


def extract_wwr_jobs(term):
    url = f"https://weworkremotely.com/remote-jobs/search?term={term}"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
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
                    "company": company.string,
                    "position": title.string,
                    "location": region.string,
                }
                results.append(job_data)
    else:
        print("Can't get jobs.")
    return results


app = Flask("JobScrapper")
db = {}


@app.route("/")
def home():
    return render_template("home-pys07.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword is None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        jobs = extract_jobs(keyword)
        jobs += extract_wwr_jobs(keyword)
        db[keyword] = jobs
    return render_template("search-pys07.html", keyword=keyword, jobs=jobs)


app.run()
