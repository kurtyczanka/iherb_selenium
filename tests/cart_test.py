from pages.cart_page import CartPage
from pages.cart_popup_page import CartPopupPage
from pages.home_page import HomePage
from tests.base_test import BaseTest


class CartTest(BaseTest):
    def test_add_product_to_cart(self):
        home_page = HomePage(self.driver)
        home_page.is_loaded()
        home_page.add_product_to_cart()

        cart_popup = CartPopupPage(self.driver)
        cart_popup.is_loaded()

        home_page.open_cart()

        cart_page = CartPage(self.driver)
        cart_page.is_loaded()

        assert cart_page.get_value_of_quantity() == "1", "Number of elements in the cart not match." \
                                                         " Expected 1, Actual: {}"\
            .format(cart_page.get_value_of_quantity())
