from browser import Browser

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.base_Page import BasePage
from pages.shoppingCartPage import Shoppingcartpage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.inventory_page = InventoryPage()
    context.base_Page = BasePage()
    context.ShoppingCartPage = Shoppingcartpage()

def after_all(context):
    context.browser.close()

