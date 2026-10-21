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
        'appPackage': 'com.mobeta.android.demodslv',
        'appActivity': 'com.mobeta.android.demodslv.Launcher',
        'noReset': True
    }

    url = "http://localhost:4724"
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    explicit_wait = WebDriverWait(driver, 15)


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



    'clicking...'
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Basic usage playground']"))).click()


    'drag and drop'
    element = explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='com.mobeta.android.demodslv:id/drag_handle']")))


    'Approach 1'

    actions = ActionChains(driver)

    screen = driver.get_window_size()
    height = screen['height']
    width = screen['width']

    endx = width/2
    endy = height*0.6

    # actions.click_and_hold(element).move_by_offset(endx, endy).release().perform()


    'Approach 2 [using javascript]'

    driver.execute_script('mobile: dragGesture',
        {
        'elementId': element,
        'endX': endx,
        'endY': endy,
        'speed': 1500
        })


