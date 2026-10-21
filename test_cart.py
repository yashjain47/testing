import pytest

@pytest.fixture()
def setUp11():
    print("Launch Browser")
    print("Login")
    print("Broswer Product")
    yield
    print("Logout")
    print("Close Browser")

def test_add_item_to_cart(setUp11):
    print("Add Item Successfully")

def test_remove_item_to_cart(setUp11):
    print("remove Item Successfully")