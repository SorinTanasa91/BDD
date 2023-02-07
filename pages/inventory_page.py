#from browser import Browser
from basePage import basePage
class InventoryPage(basePage):
    def goto_inventory_pageURL(self):
        actual= self.driver.current_url
        expected = 'https://www.saucedemo.com/inventory.html'
        assert expected == actual, f'URL diferit'
        #self.driver.url('https://www.saucedemo.com/inventory.html')
