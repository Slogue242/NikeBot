import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime
import time
import random
import config

checker = True

#generating random times for log in and such. Had to use these to prevent Nike not letting you log in.
to_logon_box = random.uniform(2.3, 4.9)
username_timeout = random.uniform(3.2, 4.8)
password_wait = random.uniform(2.1, 5.8)
hitting_enter_key = random.uniform(1.8, 3.4)
finding_size = random.uniform(1.3, 1.45)
bag_add = random.uniform(1, 1.42)

#Calling Firefox as driver to run headless
driver = webdriver.Firefox(executable_path="geckodriver.exe")
#Loading wellington rubbish website
site = "https://www.nike.com/nz/launch"
driver.get(site)
time.sleep(to_logon_box)

#find the log on button
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/header/div[1]/section/ul/li[1]/button").click()
username_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "emailAddress"))
    )
#Sleeping the program before entering the username
time.sleep(username_timeout)
username_box.send_keys(config.username)

password_box = WebDriverWait(driver, 5).until(
		EC.presence_of_element_located((By.NAME, "password"))
	)

#Sleeping the program before entering the password
time.sleep(password_wait)
password_box.send_keys(config.password)
#Sleeping the program before hitting the neter key to log in
time.sleep(hitting_enter_key)
password_box.send_keys(Keys.ENTER)

while checker == True:
	time_now = datetime.now()
	current_time = time_now.strftime("%H:%M:%S")
	#You can change this time below based on the release time of the shoe.
	if current_time == "22:00:00":
		#Setting checker to false
		checker = False
		#This clicks on the shoe in on the nike release page. This will need to be changed if you want to click on another shoe.
		driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/div[2]/div/section[1]/figure[2]/div/div/a/img').click()
		time.sleep(finding_size)
		#finds and click on the size 8 shoe in the list of shoe sizes selected
		buttons = driver.find_element_by_xpath('//button[text()="US 8"]')
		buttons.click()
		#Finding the Add to bag button and clicking it.
		#Putting the prorgram to sleep so it doesn't get detected as a bot or making actions too quickly.
		time.sleep(bag_add)
		add_to_bag = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/div/button")
		add_to_bag.click()
	else:
		pass