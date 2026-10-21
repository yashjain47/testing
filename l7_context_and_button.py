import time
import pytest
from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains



def test_alerts():

    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'UIAutomator2',
        'deviceName': 'Pixel_7_pro',
        'appPackage': 'com.socialnmobile.dictapps.notepad.color.note',
        'appActivity': 'com.socialnmobile.colornote.activity.Main',
        'noReset': True
    }

    url = "http://localhost:4724"
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    explicit_wait = WebDriverWait(driver, 10)


    cont_btn = driver.find_elements(AppiumBy.XPATH, "//android.widget.Button[@text='Continue']")
    if len(cont_btn) !=0:
        print("\ncont_btn Found!!!")
        cont_btn[0].click()

    try:
        upd_btn = explicit_wait.until(ec.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[@text='OK']")))
        if upd_btn:
            print("upd_btn Found!!!")
            upd_btn.click()
    except Exception:
        print("skipping...")



    # click on button
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='More']/android.widget.ImageView"))).click()

    # click on button
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Like us on Facebook']"))).click()


    print(driver.context)
    print(driver.contexts)



    # for back button
    'driver.back() works for returning to a previous screen inside your application, using the explicit Android keycode sends a native system event that can even exit or minimize apps'
    driver.back()


    'Simulates pressing the physical/virtual Back button'
    # driver.press_keycode(4)

    'Simulates pressing the physical/virtual Home button'
    # driver.press_keycode(3)

    'Simulates pressing the App Switcher / Overview button'
    # driver.press_keycode(187)



