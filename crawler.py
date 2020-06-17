from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from requests import get
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import sys

driver=webdriver.Chrome('/home/honey/Desktop/the right doctors/chromedriver')
driver.get("https://www.yelp.com/")
search =driver.find_element_by_id("find_desc")
search_location=driver.find_element_by_id("dropperText_Mast")
search.send_keys("Restaurants")
search_location.send_keys(Keys.CONTROL + "a")
search_location.send_keys("New York")
search.send_keys(Keys.RETURN)

code=[]
for i in range(0,3):
    time.sleep(5)
    code.append(driver.page_source)
    element=driver.find_element_by_xpath("//*[@id='wrap']/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[11]/span/a/span")
    element.click()

names=[]
urls=[]
for a in code:
    soup=BeautifulSoup(a,"html.parser")
    for i in soup.findAll("a",class_="lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE")[2:32]:
        names.append(i.get_text())
        urls.append(i["href"])


lst=[]
for i in range(0,2):
    print("retriving code of",names[i])
    driver.get("https://www.yelp.com{}".format(urls[i]))
    lst.append(driver.page_source)
    for i in range(0,2):
        element=driver.find_element_by_xpath("//*[@id='wrap']/div[4]/div/div[4]/div/div/div[2]/div[1]/div[3]/section[2]/div[2]/div/div[4]/div[1]/div/div[11]/span/a/span")
        element.click()
        time.sleep(5)
        lst.append(driver.page_source)
driver.close()
print(len(lst))

for i in lst:
    soup=BeautifulSoup(i,"html.parser")
    print(soup.find("h1",class_="lemon--h1__373c0__2ZHSL heading--h1__373c0__dvYgw undefined heading--inline__373c0__10ozy").get_text())
    print()
    for j in soup.findAll("span",class_="lemon--span__373c0__3997G raw__373c0__3rKqk")[2:]:
        print(j.get_text())
        print()
        print()
        print()
