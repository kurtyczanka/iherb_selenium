from pages.home_page import HomePage
from pages.search_page import SearchPage
from tests.base_test import BaseTest


class ProductTest(BaseTest):
    def test_add_product_to_cart_from_product_page(self):
        home_page = HomePage(self.driver)
        home_page.is_loaded()
        home_page.search_product("Carmex strawberry 10g")

        search_page = SearchPage(self.driver)
        search_page.is_loaded()
        search_page.searched_product.click()

