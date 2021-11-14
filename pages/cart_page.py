from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from timeouts import Timeouts


class CartPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

        self.CART__PAGE = By.ID, "mainCartContainer"

        self.CART__SUMMARY = By.ID, "summary"

        self.SECTION__PRODUCT_LIST = By.CSS_SELECTOR, "div[data-qa-element='cart-product-list-wrapper']"

        self.PRODUCT__QUANTITY = By.CSS_SELECTOR, "div[data-qa-element='line-item'] a[data-ga-quantity]"

        self.SECTION__SHIPPING = By.ID, "shipping"

        self.SECTION__RECOMMENDATIONS = By.CSS_SELECTOR, "div[data-qa-element='product-recommendations-wrapper']"

        self.CART__FOOTER = By.ID, "cart-footer-wrap"

    @property
    def cart__page(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.CART__PAGE), "Cart page not found"
        )

    @property
    def cart__summary(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.CART__SUMMARY), "Cart summary not found"
        )

    @property
    def section__product_list(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.CART__PAGE), "Section product list not found"
        )

    @property
    def product__quantity(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.PRODUCT__QUANTITY), "Product quantity not found"
        )

    @property
    def section__shipping(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.SECTION__SHIPPING), "Section shipping not found"
        )

    @property
    def section__recommendations(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.SECTION__RECOMMENDATIONS), "Section product recommendations not found"
        )

    @property
    def cart__footer(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.CART__FOOTER), "Section cart footer not found"
        )

    def is_loaded(self):
        assert self.cart__page
        assert self.cart__summary
        assert self.section__product_list
        assert self.product__quantity
        assert self.section__shipping
        assert self.section__recommendations
        assert self.cart__footer

    def get_value_of_quantity(self):
        return self.product__quantity.get_attribute("data-ga-quantity")



