from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageCommonMethods:
    def __init__(self, driver):
        self.loading = (By.XPATH, '//div[@id="fancybox-loading"]')
        self.layer_cart_poster = (By.ID, 'layer_cart')
        self.driver = driver

    def wait_loading(self):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.loading))

    def wait_layer_cart(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.layer_cart_poster))

    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def wait_presence(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def close_browser(self):
        self.driver.close()
        self.driver.quit()



