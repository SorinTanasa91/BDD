from browser import Browser
class InventoryPage(Browser):
    def goto_inventory_pageURL(self):
        actual= self.driver.current_url
        expected = 'https://www.saucedemo.com/inventory.html'
        assert expected == actual, f'URL diferit'
        #self.driver.url('https://www.saucedemo.com/inventory.html')
