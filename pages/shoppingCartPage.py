from pages.base_Page import BasePage

class Shoppingcartpage(BasePage):
    def getShoppingCartURL(self):
        actual = self.driver.current_url
        expected = 'https://www.saucedemo.com/cart.html'
        assert expected == actual, f'URL diferit'