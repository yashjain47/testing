import pytest
from selenium import webdriver
# pytest test_fixture_class.py -v -s --html=test_fixture.html

@pytest.fixture(scope="class")
def init_chrome_driver(request):
    ch_driver=webdriver.Chrome()
    request.cls.driver=ch_driver
    yield
    ch_driver.close()
    
@pytest.fixture(scope="class")
def init_firefox_driver(request):
    ff_driver=webdriver.Chrome()
    request.cls.driver=ff_driver
    yield
    ff_driver.close()
    
    
      
@pytest.mark.usefixtures("init_chrome_driver")
class Base_chrome_test:
    pass

class Test_Google_Chrome(Base_chrome_test):
    def test_google_title_chrome(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"
        
    
@pytest.mark.usefixtures("init_firefox_driver")
class Base_firefox_test:
    pass

class Test_Google_firefox(Base_firefox_test):
    def test_google_title_firefox(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"