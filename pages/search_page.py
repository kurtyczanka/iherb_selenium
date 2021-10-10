from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.PRODUCT__PAGE = By.ID, "ProductsPage"

        self.SEARCHED__PRODUCTS = By.CSS_SELECTOR, "div.products div.product"

        self.NUMBER_OF_DISPLAYED_ITEMS = By.CSS_SELECTOR, "select[aria-label='Display Number of Items']"

        self.PRODUCT__TITLE = By.CSS_SELECTOR,

    @property
    def product__page(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCT__PAGE))

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

    def is_loaded(self):
        assert self.product__page

    def count_searched_products(self):
        return len(self.searched__products)

    def get_number_of_displayed_items(self):
        return int(self.number_of_displayed_items.get_attribute('value'))



