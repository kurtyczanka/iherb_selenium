from pages.home_page import HomePage
from tests.base_test import BaseTest


class SearchTest(BaseTest):
    def test(self):
        page = HomePage(self.driver)
        page.is_loaded()
        page.input_search_product()

