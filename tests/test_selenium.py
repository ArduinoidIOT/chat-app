from flask import url_for
from tests.selenium_functions import *
from selenium.webdriver.support.ui import WebDriverWait


def test_register(selenium, live_server):
    selenium.get(url_for('sign_up', _external=True))
