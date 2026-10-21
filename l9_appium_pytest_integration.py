import time
import pytest
from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException



def setup_function(function):

    print("Setting UP...........")

    global driver, explicit_wait

    # global appium_service
    # appium_service = AppiumService()
    # appium_service.start()


    cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': 'UIAutomator2',
            'deviceName': 'Pixel_7_pro',
            'appPackage': 'com.google.android.contacts',
            'appActivity': 'com.android.contacts.activities.PeopleActivity',
            'noReset': False
        }
    
    url = "http://localhost:4724"
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    explicit_wait = WebDriverWait(driver, 10)
    

def teardown_function(function):

    print("Tearning Down...........")

    driver.quit()
    # appium_service.stop()
    

def test_addcontact():
    
    # click on Add button
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Create contact"))).click()

    driver.implicitly_wait(10)

    # Filling details
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='First name']"))).send_keys("Yash")
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Last name']"))).send_keys("Jain")

    # Clicking on Save button
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(4)'))).click()

