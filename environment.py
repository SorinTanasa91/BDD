from browser import Browser
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.inventory_page = InventoryPage()
def after_all(context):
    context.browser.close()

