import pytest
from typing import Any, Dict 
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 



@pytest.mark.chrome_check
@pytest.mark.skip
def test_chrome():
    ''' Finding Chrome Browser. '''

    capabilities: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'UIAutomator2',
        'deviceName': 'Pixel_7_pro',
    }

    url = "http://localhost:4724"
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(capabilities))
    wait = WebDriverWait(driver, 10)


    # elements = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Chrome')))
    elements = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "Chrome")
    # print(elements, type(elements))
    assert len(elements)!=0, "Chrome not Found!!!"

    



