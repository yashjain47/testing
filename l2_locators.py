"""
**************************************************************
************************** Locators **************************
**************************************************************

1.  Accessibility ID    >>  Non-Duplicate
2.  ID                  >>
3.  XPATH               >>  //tagname[@attribute='value']
4.  elementId           >>
5.  package             >>
6.  class               >>
7.  text                >>
8.  content-desc        >>
9.  resource-id         >>


tagname =   ClassName
attribute   =   particular attribute like text, content-desc, package.





**************************************************************
**************************** Wait ****************************
**************************************************************


1. Implicit waits
    driver waits for whole window (fixed wait) like time.sleep
    driver.implicit_wait(5)

2. Explicit waits
    wait for a particular condition

    explicit_wait = WebDriverWait(driver, 10)
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Create contact"))).click()

3. Fluent waits 
    flueent_wait = = WebDriverWait(driver, 10)

    fluent_wait = WebDriverWait(driver, 10, poll_frequency=11, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])




"""



import time
import pytest
from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

@pytest.mark.skip
def test_chrome_searchBox():
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'UIAutomator2',
        'deviceName': 'Pixel_7_pro',
    }

    # URL [Current : local]
    url = "http://localhost:4724"

    # Web driver
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

    # Webdriver wait
    explicit_wait = WebDriverWait(driver, 10)

    # By Accessibility ID
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Chrome"))).click()

    # By Xpath
    driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Search Google or type URL']").send_keys("Yash Jain")

    driver.implicitly_wait(3)
    driver.quit()


@pytest.mark.skip
def test_phonecall():
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'UIAutomator2',
        'deviceName': 'Pixel_7_pro',
        'appPackage': 'com.google.android.dialer',
        'appActivity': 'com.android.dialer.main.impl.MainActivity',
        'noReset': True
    }

    # URL [Current : local]
    url = "http://localhost:4724"

    # Web driver
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

    # Webdriver wait
    explicit_wait = WebDriverWait(driver, 10)

    # keypad click
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Keypad']"))).click()

    time.sleep(10)
    # dialing numbers 12345
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.google.android.dialer:id/dialpad_key_number" and @text="1"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.google.android.dialer:id/dialpad_key_number" and @text="2"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.google.android.dialer:id/dialpad_key_number" and @text="3"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.google.android.dialer:id/dialpad_key_number" and @text="4"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.google.android.dialer:id/dialpad_key_number" and @text="5"]').click()

    driver.implicitly_wait(3)

    # click on call button
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Call"]').click()

    driver.implicitly_wait(3)
    driver.quit()


@pytest.mark.skip
def test_addcontact():
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

    # click on Add button
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Create contact"))).click()

    driver.implicitly_wait(10)

    # Filling details
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='First name']"))).send_keys("Yash")
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Last name']"))).send_keys("Jain")

    # explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().className("android.view.View").instance(26)'))).send_keys("7689911101")
    

    # Clicking on Save button
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(4)'))).click()





