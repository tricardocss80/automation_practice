from selenium.webdriver.common.by import By
from pagecommonmethods import PageCommonMethods


class PageCart(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.quantity_cart = (By.ID, 'layer_cart_product_quantity')
        self.check_shipping = (By.XPATH, '//span[@class="ajax_cart_shipping_cost"]')
        self.checks_total_price_product = (By.ID, 'layer_cart_product_price')
        self.checks_total_cart_price = (By.XPATH, '//span[@class="ajax_block_cart_total"]')
        self.product_name = (By.ID, 'layer_cart_product_title')
        self.driver = driver

    def checks_quantity_products(self):
        return int(self.wait_presence(self.quantity_cart).text)

    def checks_total_price_products(self):
        return float(self.wait_presence(self.checks_total_price_product).text.replace('$', ''))

    def checks_shipping(self):
        return float(self.wait_presence(self.check_shipping).text.replace('$', ''))

    def check_total_cart_price(self):
        return float(self.wait_presence(self.checks_total_cart_price).text.replace('$', ''))

    def checks_product_name(self):
        return self.wait_presence(self.product_name).text



