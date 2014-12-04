from selenium import webdriver

def test_broswer_has_django_in_the_title():
    browser = webdriver.Firefox()
    browser.get('http://localhost:8000')
    assert 'Django' in browser.title
