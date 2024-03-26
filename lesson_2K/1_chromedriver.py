import time
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.walmart.com/")
Page_URL = driver.current_url
print(Page_URL)
#Page_Source = driver.page_source
#print(Page_Source)
time.sleep(2)
Page_title = driver.title
print(Page_title)
driver.get("https://flukeout.github.io/")
time.sleep(5)
Page_title1 = driver.title
print(Page_title1)
driver.back()
assert driver.title == "Walmart | Save Money. Live better.", "Страница не открылась"
time.sleep(5)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.back()
time.sleep(2)
driver.refresh()



