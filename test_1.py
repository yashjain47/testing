# import time
# from selenium import webdriver

# a=webdriver.Chrome()
# print("asasas",a)
# time.sleep(5)
# print("Printing")
##################################################################################################

# file name should start with test or # ends with test
# function name should always starts with test

# run the file like
# py.test or pytest                            ---> for all files 
# py.test test_1.py ,py.test test_2.py or      ---> for particular files
# py.test /PYTHON/test_1.py
# py.test -k login -v                          ---> for functions  starts with "login" name
# pytest -v                                    ---> for details

# -v is for verbosity
# -k is for name (only run tests which match the given substring.)
# -m is for markexpr or mark (only run tests matching given mark expression.)
# eg pytest -m m         --> here 'm' is the mark 

 
# assert is the aseertion used to show the error

import pytest

def test1():
    a=3
    b=4
    c=3
    assert a==b,"Test Failed"
    assert a==c,"Test Failed as A is not equal to b"

@pytest.mark.m
def test2():
    name="yash"
    assert name.upper()=="YASH","test Failed as name"

@pytest.mark.skip
def test3():
    assert True
    
@pytest.mark.xfail    
def test4():
    assert 100==100,"test Failed as 100"
    
@pytest.mark.m
def test5():
    assert True
    
def test_login():
    assert "yash" == "yash"