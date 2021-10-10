from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, context):
        super().__init__(context)

        self.SEARCH__FIELD = By.CSS_SELECTOR, "input.iherb-header-search-input"

        self.HOME__PAGE = By.ID, "iherb-homepage"

        self.HOME__PAGE_BANNER = By.CSS_SELECTOR, "div.hp-banners-container"

    @property
    def search__field(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH__FIELD))

    @property
    def home__page(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.HOME__PAGE))

    @property
    def home__page_banner(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.SEARCH__FIELD))

    def is_loaded(self):
        assert self.search__field
        assert self.home__page
        assert self.home__page_banner

    def search_product(self, product):
        self.search__field.click()
        self.search__field.send_keys(product)
        self.search__field.send_keys(Keys.ENTER)

