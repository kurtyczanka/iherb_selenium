from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
from random import choice, randrange

from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.PRODUCT__PAGE = By.ID, "ProductsPage"

        self.SEARCHED__PRODUCTS = By.CSS_SELECTOR, "div.products div.product"

        self.NUMBER_OF_DISPLAYED_ITEMS = By.CSS_SELECTOR, "select[aria-label='Display Number of Items']"

        self.SEARCHED_PRODUCT = By.CSS_SELECTOR, "div.product-cell-container"

        self.LOADER = By.CSS_SELECTOR, "div.loader.loading"

        self.PRODUCT__TITLE = By.CSS_SELECTOR,

    @property
    def product__page(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCT__PAGE), "Product page did not load")

    @property
    def searched__products(self):
        """
        :return list of searched products'
        """
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.SEARCHED__PRODUCTS))

    @property
    def number_of_displayed_items(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.NUMBER_OF_DISPLAYED_ITEMS)
        )

    @property
    def searched_product(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.SEARCHED_PRODUCT)
        )

    @property
    def loader(self):
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.LOADER)
        )

    def is_loaded(self):
        assert self.product__page

    def count_searched_products(self):
        return len(self.searched__products)

    def get_number_of_displayed_items(self):
        return int(self.number_of_displayed_items.get_attribute('value'))

    def select_number_of_product(self):
        select = Select(self.number_of_displayed_items)
        select.select_by_index(randrange(2))
        self.wait_until_loader_disappear()

    def wait_until_loader_disappear(self):
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.LOADER), "Loader is still visible"
        )

