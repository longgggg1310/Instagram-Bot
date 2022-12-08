import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

# 0. Declare the browser
browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

# 1. Open faceboook
browser.get("https://www.instagram.com")
sleep(2)
fb_login = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[5]/button').click()
# 2. Truy to login

txtUser = browser.find_element(By.ID,"email")
txtUser.send_keys("")

txtPassword = browser.find_element(By.ID,"pass")
txtPassword.send_keys("")

txtPassword.send_keys(Keys.ENTER)

sleep(10)

pickle.dump(browser.get_cookies(), open("my_cookie1.pkl","wb"))

browser.close()