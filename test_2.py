import pytest

@pytest.mark.yas
def test6():
    assert "yash".lower()=="yash","Test failed as lower letters "
    
def test7():
    assert 10==5+5,"Test failed as addition"

@pytest.mark.m    
def test_login():
    assert "yash" == "yash"