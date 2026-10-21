from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('launch Chrome Browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window() 

@when('Open orangehrm homepage')
def open_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then('verify the logo present on page')
def verify_logo(context):
    logo_xpath = "//div[contains(@class, 'orangehrm-login-branding') or @class='orangehrm-logo']//img"
    
    try:

        logo_element = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, logo_xpath))
        )
        status = logo_element.is_displayed()
    except Exception:
        status = False
        
    print(f"Status: {status}")
    assert status is True, "Validation Failed: The OrangeHRM branding logo element was not displayed on the screen."

@then('Close Browser')
def close_browser(context):
    context.driver.quit()

