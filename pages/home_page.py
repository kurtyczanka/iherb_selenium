from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from timeouts import Timeouts


class HomePage(BasePage):
    def __init__(self, context):
        super().__init__(context)

        self.SEARCH__FIELD = By.CSS_SELECTOR, "input.iherb-header-search-input"

        self.HOME__PAGE = By.ID, "iherb-homepage"

        self.HOME__PAGE_BANNER = By.CSS_SELECTOR, "div.hp-banners-container"

        self.SECTION__TRENDING_NOW = By.ID, "hp-module-trending"

        self.SECTION__BEST_SELLERS = By.ID, "hp-module-best-selling"

        self.SECTION__NEW_ARRIVALS = By.ID, "hp-module-new-arrivals"

        self.PRODUCT_TITLE = By.CSS_SELECTOR, "div.product-inner"

    @property
    def search__field(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.element_to_be_clickable(self.SEARCH__FIELD), "Search field not found"
        )

    @property
    def home__page(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.HOME__PAGE), "Home page not found"
        )

    @property
    def home__page_banner(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.HOME__PAGE_BANNER), "Home page banner not found"
        )

    @property
    def section__trending_now(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.SECTION__TRENDING_NOW), "Section 'trending now' not found"
        )

    @property
    def section__best_sellers(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.SECTION__BEST_SELLERS), "Section 'best sellers' not found"
        )

    @property
    def section__new_arrivals(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.visibility_of_element_located(self.SECTION__NEW_ARRIVALS), "Section 'new arrivals' not found"
        )

    @property
    def product_title(self):
        return WebDriverWait(self.driver, Timeouts.element_search_expected_conditions).until(
            EC.element_to_be_clickable(self.PRODUCT_TITLE), "Product title not found"
        )

    def is_loaded(self):
        assert self.search__field
        assert self.home__page
        assert self.home__page_banner
        assert self.section__trending_now
        assert self.section__best_sellers
        assert self.section__new_arrivals

    def search_product(self, product):
        self.search__field.click()
        self.search__field.send_keys(product)
        self.search__field.send_keys(Keys.ENTER)

    def open_product_page_trending_now(self):
        self.product_title.click()


