from browser import browser
class InventoryPage(browser):
    def goto_inventory_pageURL(self):
        return self.driver.current_url
        #self.driver.url('https://www.saucedemo.com/inventory.html')
