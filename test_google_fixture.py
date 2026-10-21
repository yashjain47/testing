from selenium import webdriver
import pytest
# pip install pytest-html pytest-xdist
# pytest -s test_google_fixture.py 

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("----------------setup----------------")
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")
    
    yield
    print("----------------tear down----------------")
    driver.quit()
   
def test_title(init_driver):
    print("Test_title")
    driver.title=="Google"
    
def test_url(init_driver):
    print("Test_url")
    driver.current_url=="Google.com","Url Failed"