from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
user = ""
pwd = ""
chrome_path = "G:/Local disk/selenium/chrome/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

website_URL = "https://www.google.co.in/"
driver.get(website_URL)


refreshrate = int(1)
count=0
# This would keep running until you stop the compiler.
while count<3:
    time.sleep(refreshrate)
    driver.refresh()
    count=count+1



driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()