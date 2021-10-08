from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, context):
        super().__init__(context)

        self.SEARCH__FIELD = By.CSS_SELECTOR, "input.iherb-header-search-input"

    @property
    def search__field(self):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.SEARCH__FIELD))

    def is_loaded(self):
        assert self.search__field

    def input_search_product(self):
        self.search__field.click()
        self.search__field.send_keys("Shampoo")

