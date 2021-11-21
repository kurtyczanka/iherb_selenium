from pages.cart_popup_page import CartPopupPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.top_menu_page import TopMenuPage
from tests.test_base import BaseTest


class ProductTest(BaseTest):
    def test_title_on_product_page_match_title_on_home_page(self):
        home_page = HomePage(self.driver)
        home_page.is_loaded()
        title_on_home_page = home_page.get_product_title()

        home_page.open_product_page_trending_now()

        product_page = ProductPage(self.driver)
        product_page.is_loaded()
        title_on_product_page = product_page.get_title()

        assert title_on_product_page == title_on_home_page, "Title on product page is different than title on" \
                                                            "home page. Expected: {}, Actual: {}" \
            .format(title_on_home_page, title_on_product_page)

    def test_add_product_to_cart_from_product_page(self):
        home_page = HomePage(self.driver)
        home_page.is_loaded()

        home_page.open_product_page_trending_now()

        product_page = ProductPage(self.driver)
        product_page.is_loaded()

        product_page.add_product_to_cart()

        cart_popup = CartPopupPage(self.driver)
        assert cart_popup.get_value_of_cart_popup_display() == "block", "Cart popup did not display. Expected 'block'" \
                                                                        "css style. Actual: {}"\
            .format(cart_popup.get_value_of_cart_popup_display())

        top_menu = TopMenuPage(self.driver)
        assert top_menu.get_cart_quantity() == "1", "Expected one product in the cart. Actual: {}"\
            .format(top_menu.get_cart_quantity())

