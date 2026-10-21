from behave import *
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()


@given('launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    # context.driver.maximize_window()


@when('open orangehrm page')
def step_impl(context):
    context.exp_wait = WebDriverWait(context.driver, 10)
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('enter username "{name}" and password "{password}"')
def step_impl(context, name, password):
    
    context.exp_wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(name)
    context.exp_wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)

@when('click on login button')
def step_impl(context):
    context.exp_wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Login']"))).click()
    

@then('user must successfully login to the dashboard')
def step_impl(context):
    
    try:
        context.driver.implicitly_wait(2)
        dashbord = context.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
    
    except:
        context.driver.close()
        assert False, "Login Failed"

    if dashbord == "Dashboard":
        assert True, "Login Successful"
        context.driver.close()
    