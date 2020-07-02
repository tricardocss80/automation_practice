from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from automation_practice.pagecommonmethods import PageCommonMethods


class PagePrintedDresses(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.unit_price = (By.XPATH, '//div[@class="price"]')
        self.button_plus = (By.XPATH, '//i[contains(@class,"icon-plus")]')
        self.select_size = (By.XPATH, '//select[contains(@id,"1")]')
        self.button_click_add_to_card = (By.XPATH, '//span[contains(.,"Add to cart")]')
        self.driver = driver

    def add_dresses(self, quantity):
        for i in range(quantity):
            self.wait_clickable(self.button_plus).click()

    def price_product(self):
        return float(self.wait_presence(self.unit_price).text.replace('$', ''))

    def selects_size(self, value):
        Select(self.wait_presence(self.select_size)).select_by_value(value)

    def click_add_to_card(self):
        self.wait_clickable(self.button_click_add_to_card).click()

