from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from timeouts import Timeouts


class ProductPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

        self.PRODUCT__DETAILS = By.CSS_SELECTOR, "div.product-detail-container"

        self.PRODUCT__IMAGE = By.ID, "iherb-product-image"

        self.PRODUCT__SPECS = By.ID, "product-specs-list"

        self.SECTION__RELATED_PRODUCTS = By.ID, "related-products-wrapper"

        self.SECTION__PRICING = By.ID, "pricing"

        self.SECTION__PRODUCT_FORM = By.ID, "product-form"

        self.BUTTON__ADD_TO_CART = By.CSS_SELECTOR, "button.btn-add-to-cart"


    @property
    def product__details(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.PRODUCT__DETAILS), "Product details is not found"
        )

    @property
    def product__image(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.PRODUCT__IMAGE), "Product image is not found"
        )

    @property
    def product__specs(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.PRODUCT__SPECS), "Product specs is not found"
        )

    @property
    def section__related_products(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.SECTION__RELATED_PRODUCTS), "Section related products is not found"
        )

    @property
    def section__pricing(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.SECTION__PRICING), "Section product form is not found"
        )

    @property
    def section__product_form(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.SECTION__PRODUCT_FORM), "Section product page is not found"
        )

    @property
    def button__add_to_cart(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.BUTTON__ADD_TO_CART), "Button add to cart is not found"
        )

    def is_loaded(self):
        assert self.product__details
        assert self.product__image
        assert self.product__specs
        assert self.section__related_products
        assert self.section__pricing
        assert self.section__product_form
        assert self.button__add_to_cart

    def add_product_to_cart(self):
        self.button__add_to_cart.click()
