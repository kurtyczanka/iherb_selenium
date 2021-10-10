from pages.home_page import HomePage
from pages.search_page import SearchPage
from tests.base_test import BaseTest


class SearchTest(BaseTest):
    def verify_searched_product_displayed(self):
        home_page = HomePage(self.driver)
        home_page.is_loaded()
        home_page.search_product("Carmex strawberry 10g")

        search_page = SearchPage(self.driver)
        search_page.is_loaded()

        assert len(search_page.searched__products) == 1

    def test_number_of_searched_products_is_equal_to_selected(self):
        home_page = HomePage(self.driver)
        home_page.is_loaded()
        home_page.search_product("Shampoo")

        search_page = SearchPage(self.driver)
        search_page.is_loaded()

        assert search_page.count_searched_products() == search_page.get_number_of_displayed_items(), \
            "Number of displayed elements is different than number of expected product on page. Expected: {}, " \
            "Actual: {}".format(search_page.get_number_of_displayed_items(), search_page.count_searched_products())
