from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from timeouts import Timeouts


class ProductReviewPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

        self.PRODUCT__REVIEW_PAGE = By.ID, "review-model"

        self.HOME__PAGE = By.ID, "iherb-homepage"

        self.HOME__PAGE_BANNER = By.CSS_SELECTOR, "div.hp-banners-container"

    @property
    def product__review_page(self):
        return WebDriverWait(self.driver, Timeouts.base_timeout).until(
            EC.visibility_of_element_located(self.PRODUCT__REVIEW_PAGE), "Product page is not")

    def is_loaded(self):
        assert self.product__review_page
