from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
# pip install pytest-html pytest-xdist

driver = None

def setup_module(module):
    global driver
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")
    
def teardown_module(module):
    driver.quit()
   
def test_title():
    driver.title=="Google"
    
def test_url():
    driver.current_url=="Google.com","Url Failed"