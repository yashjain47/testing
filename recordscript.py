from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'UIAutomator2',
    'deviceName': 'Pixel_7_pro',
    'appPackage': 'com.google.android.contacts',
    'activityPackage': 'com.android.contacts.activities.PeopleActivity}',
    'noReset': False
}

url = "http://localhost:4724"
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
explicit_wait = WebDriverWait(driver, 10)

el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create contact")
el5.click()
el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text('First name')")
el6.send_keys("Tushar")
el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text('Last name')")
el7.send_keys("Jain")
el8 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className('android.widget.Button').instance(4)")
el8.click()






