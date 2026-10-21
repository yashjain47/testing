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


@pytest.mark.skip
def test_scrollintoview():
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'UIAutomator2',
        'deviceName': 'Pixel_7_pro',
        'appPackage': 'com.hmh.api',
        'appActivity': '.ApiDemos',
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



    # click on App button
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='App']"))).click()

    # click on Activity button
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Activity']"))).click()



    wallpaper_selector = (
        'new UiScrollable(new UiSelector().scrollable(true))'
        '.scrollIntoView(new UiSelector().text("Wallpaper"))'
    )
    
    # scroll till Wallpaper is shown...
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, wallpaper_selector))).click()
    
    print("Scrolled and clicked on Wallpaper successfully!")
    time.sleep(2)


@pytest.mark.skip
def test_vertical_scroll():
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'UIAutomator2',
        'deviceName': 'Pixel_7_pro',
        'appPackage': 'com.hmh.api',
        'appActivity': '.ApiDemos',
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



    # click on App button
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='App']"))).click()

    # click on Activity button
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Activity']"))).click()



    'Approach 1 [Using built-In Functions]'

    # scroll Down...
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(5)')))

    # scroll Up...
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToBeginning(5)')))
    

    


    'Approach 2 [By X and Y coordinates]   [Not Recommended as TouchAction not supported in python 2x or 3x]'

    # device_size = driver.get_window_size()
    # print(device_size)

    # screen_width = device_size['width']
    # screen_height = device_size['height']

    # print(screen_height, screen_width)

    # startx = screen_width/2
    # endx = screen_width/2
    # starty = screen_height*8/9
    # endy = screen_height/9

    # actions = TouchAction(driver)

    # # scroll Down
    # actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()

    # # scroll Up
    # actions.long_press(None, endx, endy).move_to(None, startx, starty).release().perform()



def test_horizontal_scroll():
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'UIAutomator2',
        'deviceName': 'Pixel_7_pro',
        'appPackage': 'com.hmh.api',
        'appActivity': '.ApiDemos',
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



    # click on Views button
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Views']"))).click()

    # click on Gallery button
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Gallery']"))).click()

    # click on 1. Photos button
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='1. Photos']"))).click()



    'scroll Left...'
    # explicit_wait.until(ec.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToEnd(5)')))
    'OR'
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollForward(5)')))
    




    'scroll Right...'
    # explicit_wait.until(ec.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToBeginning(5)')))
    'OR'
    explicit_wait.until(ec.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollBackward(5)')))
    

    

