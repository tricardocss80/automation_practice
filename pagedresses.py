from selenium.webdriver.common.by import By
from pagecommonmethods import PageCommonMethods
from selenium.webdriver.support.ui import Select


class PageDresses(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.button_casual_dresses = (By.XPATH, '//div[@class="block_content"]//ul[@class="tree dynamized"]'
                                                '//a[contains(text(),"Casual Dresses")]')
        self.select_order_price = (By.XPATH, '//select[contains(@id,"selectProductSort")]')
        self.icon_list = (By.XPATH, '//i[contains(@class,"icon-th-list")]')
        self.driver = driver

    def select_casual_dresses(self):
        self.wait_clickable(self.button_casual_dresses).click()

    def select_by_price(self, index):
        Select(self.wait_presence(self.select_order_price)).select_by_index(index)

    def list_view(self):
        self.wait_clickable(self.icon_list).click()

