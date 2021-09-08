from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import MainPageLocators


class MainPage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.SIGN_IN_LINK).click()

    def go_to_cart(self):
        self.browser.find_element(*MainPageLocators.CART_LINK).click()
