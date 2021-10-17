from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from timeouts import Timeouts


class TopMenuPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

        self.CART__QUANTITY = By.ID, "cart-qty"

    @property
    def cart__quantity(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.CART__QUANTITY))

    def get_cart_quantity(self):
        return self.cart__quantity.text
