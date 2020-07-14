from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

driver=webdriver.Chrome('/home/honey/Desktop/the right doctors/chromedriver')
driver.get("https://www.yelp.com/")
search =driver.find_element_by_id("find_desc")
search_location=driver.find_element_by_id("dropperText_Mast")

x=input("enter what you want to find:")
y=input("enter location:")
search.send_keys(x)
search_location.send_keys(Keys.CONTROL + "a")
search_location.send_keys(y)
search.send_keys(Keys.RETURN)

hotels_urls=[]
hotels=[]
for i in range(6,36):
	hotels.append(driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/ul/li[{}]/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/h4/span/a".format(i)).text)
	hotels_urls.append(driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/div[1]/div[1]/div[2]/div[2]/ul/li[{}]/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/h4/span/a".format(i)).get_attribute("href"))

reviews=[]
ratings=[]
name=[]
for url in hotels_urls[1:]:
	driver.get(url)
	#driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div/div/div/div/div[2]/div[4]/button").click()
	try:

		for j in range(10):
			time.sleep(3)
			for i in range(1,21):
				name.append(driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/h1").text)
				ratings.append(driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/section[2]/div[2]/div/ul/li[{}]/div/div[2]/div[1]/div/div[1]/span/div".format(i)).get_attribute("aria-label").split()[0])
				try:
					reviews.append(driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/section[2]/div[2]/div/ul/li[{}]/div/div[2]/div[3]/p/span".format(i)).text)
				except:
					reviews.append(driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/section[2]/div[2]/div/ul/li[{}]/div/div[2]/div[2]/p/span".format(i)).text)
				print("data extracted.......")

			driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/section[2]/div[2]/div/div[4]/div[1]/div/div[11]/span/a/span").click()
	except:
		continue
driver.close()

