from pagecommonmethods import PageCommonMethods
from selenium.webdriver.common.by import By


class PageOperations(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.price_product = (By.XPATH, '//div[@class="price"]')
        self.driver = driver

    def price_products(self):
        return float(self.wait_presence(self.price_product).text.replace('$', ''))

