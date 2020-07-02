from selenium.webdriver.common.by import By
from automation_practice.pagecommonmethods import PageCommonMethods


class PageIndex(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.button_section_dresses = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a')
        self.button_sin_in = (By.XPATH, '//a[@class="login"]')
        self.driver = driver

    def enter_dresses_section(self):
        self.wait_clickable(self.button_section_dresses).click()