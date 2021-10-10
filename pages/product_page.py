from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

        self.PRODUCT__PAGE = By.ID, "review-model"

        self.HOME__PAGE = By.ID, "iherb-homepage"

        self.HOME__PAGE_BANNER = By.CSS_SELECTOR, "div.hp-banners-container"

    @property
    def product__page(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCT__PAGE))

    def is_loaded(self):
        assert self.product__page
