from selenium.webdriver.common.by import By
from pagecommonmethods import PageCommonMethods


class PageCasualDresses(PageCommonMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.printed_Dress_elemenent = (By.XPATH, '//img[@title="Printed Dress"]')
        self.driver = driver

    def select_dress(self):
        self.wait_clickable(self.printed_Dress_elemenent).click()



