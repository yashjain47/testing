import webdriver_manager
from selenium import webdriver

# to run parallel use -n 2 (here 2 is the number of threads )
# example --> py.test test_webpage.py -n 2 (2 is the number of browser or windows )


def test_google():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.google.com")
    assert driver.title == "Google","Google Failed"
    driver.quit()
    
def test_gmail():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.Gmail.com")
    assert driver.title == "Gmail","Gmail Failed"
    driver.quit()
