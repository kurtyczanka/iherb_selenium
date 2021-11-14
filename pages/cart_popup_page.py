from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from timeouts import Timeouts


class CartPopupPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.CART__CONTAINER = By.CSS_SELECTOR, "section.add-to-cart-container"

    @property
    def cart__container(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.CART__CONTAINER))

    def get_value_of_cart_popup_display(self):
        return self.cart__container.value_of_css_property("display")

    def is_loaded(self):
        assert self.cart__container
