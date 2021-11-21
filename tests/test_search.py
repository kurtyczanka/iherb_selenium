from constants import Constants
from pages.cart_popup_page import CartPopupPage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.top_menu_page import TopMenuPage
from tests.test_base import BaseTest


class SearchTest(BaseTest):
    def test_004_searched_product_displayed(self):
        home_page = HomePage(self.driver)
        home_page.is_loaded()
        home_page.search_product(Constants.particular__product)

        search_page = SearchPage(self.driver)
        search_page.is_loaded()

        assert len(search_page.searched__products) == 1, "Expected one product on page. Actual: {}".format(
            len(search_page.searched__products))

    def test_005_number_of_searched_products_is_equal_to_selected(self):
        home_page = HomePage(self.driver)
        home_page.is_loaded()
        home_page.search_product(Constants.product__category)

        search_page = SearchPage(self.driver)
        search_page.is_loaded()
        search_page.select_number_of_product()

        assert search_page.count_searched_products() == search_page.get_number_of_displayed_items(), \
            "Number of displayed elements is not match. Expected: {}, Actual: {}".format(
                search_page.get_number_of_displayed_items(), search_page.count_searched_products())

