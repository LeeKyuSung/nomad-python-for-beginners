from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

keyword = input("What do you want to search? ")
wwr = extract_wwr_jobs(keyword)
jobs = wwr

file = open(f"{keyword}.csv", mode="w")
file.write("title,company,region,position")

for job in jobs:
    file.write(f"{job['title']},{job['company']},{job['region']},{job['position']}\n")

file.close()
