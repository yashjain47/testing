"""

if scope = "session"

output:
test_cart.py::test_add_item_to_cart Launch Browser
Login
Browser Products
Add Item Successfully
PASSED
test_cart.py::test_remove_item_to_cart remove Item Successfully
PASSEDLogoff
Close Browser

-----------------------------------------------------------------------------------

if scope = "function"

output:
test_cart.py::test_add_item_to_cart Launch Browser
Login
Browser Products
Add Item Successfully
PASSEDLogoff
Close Browser

test_cart.py::test_remove_item_to_cart Launch Browser
Login
Browser Products
remove Item Successfully
PASSEDLogoff
Close Browser


-----------------------------------------------------------------------------------

if scope = "module"

output:
Login
Browser Products
Add Item Successfully
PASSED
test_cart.py::test_remove_item_to_cart remove Item Successfully
PASSEDLogoff
Close Browser

-----------------------------------------------------------------------------------

if scope = "package"

output:
test_cart.py::test_add_item_to_cart Launch Browser
Login
Browser Products
Add Item Successfully
PASSED
test_cart.py::test_remove_item_to_cart remove Item Successfully
PASSEDLogoff
Close Browser

-----------------------------------------------------------------------------------

if scope = "class"

output:
test_cart.py::test_add_item_to_cart Launch Browser
Login
Browser Products
Add Item Successfully
PASSEDLogoff
Close Browser

test_cart.py::test_remove_item_to_cart Launch Browser
Login
Browser Products
remove Item Successfully
PASSEDLogoff
Close Browser

-----------------------------------------------------------------------------------

without scope

output:
test_cart.py::test_add_item_to_cart Launch Browser
Login
Browser Products
Add Item Successfully
PASSEDLogoff
Close Browser

test_cart.py::test_remove_item_to_cart Launch Browser
Login
Browser Products
remove Item Successfully
PASSEDLogoff
Close Browser

"""


import pytest

@pytest.fixture(scope="session",autouse=True)
def tc_setup(browser):
    if browser == "chrome":
        print("Launch Chrome")
    elif browser == "ff":
        print("Launch FireFox")
    else:
        print("Provide Valid Browser")

    print("Launch Browser")
    print("Login")
    print("Browser Products")
    yield
    print("Logoff")
    print("Close Browser")


def pytest_addoption(parser):
    parser.addoption("--browser")
    # parser.addoption("--platform")


@pytest.fixture(scope="session",autouse=True)
def browser(request):
    return request.config.getoption("--browser")
