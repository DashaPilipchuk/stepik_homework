import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket(browser):
    browser.get(link)
    time.sleep(3)
    assert browser.find_elements(by="css selector", value="#add_to_basket_form > button"), 'basket button not found'


