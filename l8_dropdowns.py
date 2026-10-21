import time
import pytest
from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException



def test_dropdowns():

    try:

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
        explicit_wait = WebDriverWait(driver, 10)

        # click on Add button
        explicit_wait.until(ec.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Create contact"))).click()

        driver.implicitly_wait(5)

        # Filling details
        explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='First name']"))).send_keys("Yash")
        explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Last name']"))).send_keys("Jain")

        explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='+1']/android.view.View[1]"))).click()


        target_text = "IN India +91"
        scroll_selector = (
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().text("{target_text}"))'
        )

        options = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_selector).click()


        num_ele = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='+91']/android.view.View[2]")
        num_ele.send_keys("7689887780")


        # Clicking on Save button
        explicit_wait.until(ec.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(4)'))).click()


    finally:
        driver.press_keycode(3)
        driver.quit()

