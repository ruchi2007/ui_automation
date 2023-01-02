import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://uat-iqrashopingdemo.ml/")
driver.implicitly_wait(5)
username="//*[@id='username-9']"
password="//*[@id='user_password-9']"
login="//*[@id='um-submit-btn']"
logout="//*[@id='menu-item-50']/a"
time.sleep(3)
driver.find_element_by_xpath(username).send_keys(" Test_user2023")
time.sleep(3)
driver.find_element_by_xpath(password).send_keys(" Test_user2023")
time.sleep(3)
driver.find_element_by_xpath(login).click()
time.sleep(3)
driver.find_element_by_xpath(logout).click()
time.sleep(3)
expected_url = "http://uat-iqrashopingdemo.ml/logout/"
actual_url = driver.current_url
driver.save_screenshot("image.png")
assert expected_url == actual_url
print(driver.current_url)
title = driver.title
print(driver.title)
actual_title = "Iqra shoping Demo"
#assert title == actual_title
driver.save_screenshot("image.png")

print(actual_url)
