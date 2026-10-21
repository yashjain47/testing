import pytest
from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains



def test_tap_and_long_press():

    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'UIAutomator2',
        'deviceName': 'Pixel_7_pro',
        'appPackage': 'com.google.android.contacts',
        'appActivity': 'com.android.contacts.activities.PeopleActivity',
        'noReset': True
    }

    url = "http://localhost:4724"
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    explicit_wait = WebDriverWait(driver, 15)

    'Opening Contact App'
    contact = explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Contacts']"))).click()


    
    'Tap on Name button'
    name = explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text, 'Yash Jain')]")))

    # name.click()
    'OR'
    # actions = ActionChains(driver)
    # actions.click(name).perform()


    'Long Press'
    name = explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text, 'Yash Jain')]")))
    actions = ActionChains(driver)
    actions.click_and_hold(name).pause(2).perform()
    






