from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

browser = webdriver.Chrome()
browser.get("https://www.indeed.com/jobs?q=python&l=Remote&limit=50")
# print(browser.page_source)

file = open("indeed.html", "w")
file.write(browser.page_source)
