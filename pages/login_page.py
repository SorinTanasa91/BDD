from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

from browser import Browser


class LoginPage(Browser):
    USERNAME_INPUT=(By.ID,"user-name")
    PASSWORD_INPUT=(By.ID,"password")
    LOGIN_BUTTON=(By.ID,'login-button')

    def __init__(self,login_button):
        self.login_button = login_button

    def go_to_login_page(self):
        self.driver.get('https://www.saucedemo.com/')
