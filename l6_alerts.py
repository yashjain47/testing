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

    try:

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
        explicit_wait.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Alert Dialogs']"))).click()

        # element
        element = explicit_wait.until(ec.presence_of_element_located((AppiumBy.ID, "com.hmh.api:id/two_buttons"))).click()
        # element = explicit_wait.until(ec.presence_of_element_located((AppiumBy.ID, "com.hmh.api:id/text_entry_button"))).click()
        	

        'alert accept'
        driver.switch_to.alert.accept()

        'alert dismiss'
        # driver.switch_to.alert.dismiss()

        'alert send text'
        # driver.switch_to.alert.send_keys("Yash")

        print(driver.switch_to.alert.text)

    except Exception as Error:
        print(f"Exception Error : {Error}")     
        driver.quit()


