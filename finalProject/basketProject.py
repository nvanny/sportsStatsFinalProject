from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("https://www.basketball-reference.com/leagues/NBA_2019.html#all_team-stats-base")
content = driver.page_souce
soup = BeautifulSoup(content)
type(soup)
title = soup.title
print(title)
#print(soup.text)
