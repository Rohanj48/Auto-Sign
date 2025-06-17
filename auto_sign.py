from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
    "clientHints": {"platform": "Android", "mobile": True}}

chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

service = Service(executable_path='chromedriver-win64\\chromedriver.exe')

driver = webdriver.Chrome(
    service=service,
    options=chrome_options)

driver.get("url")


user = {"username": "", "password": ""}

user_form = driver.find_element(By.ID, 'username')
pass_form = driver.find_element(By.ID, 'password')
submit_button = driver.find_element(By.ID, 'loginbutton')


user_form.send_keys(user["username"])
pass_form.send_keys(user["password"])
submit_button.click()
time.sleep(0.5)
driver.quit()
quit()
