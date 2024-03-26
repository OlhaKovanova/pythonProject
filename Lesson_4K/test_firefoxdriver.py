from datetime import time
import pytest

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
def test_1():
    driver.get("https://www.walmart.com/")
#time.sleep(2)
    page_title1 = driver.title
    print(page_title1)
    driver.get("https://www.wikipedia.org/")
    page_title2 = driver.title
    print(page_title2)
    driver.back()
    assert driver.title == "Walmart | Save Money. Live better.", "Page is not opened"
    driver.refresh()
    website_url1 = driver.current_url
    print(website_url1)
    driver.forward()
    assert driver.current_url == "https://www.wikipedia.org/", "there is another url"
    driver.quit()
