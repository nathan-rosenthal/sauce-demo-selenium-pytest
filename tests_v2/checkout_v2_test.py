import allure
from allure_commons.types import Severity


class TestCheckout:

    @allure.severity(Severity.CRITICAL)
    @allure.description("Add a single item to cart and checkout")
    @allure.title("Checkout a single item")
    def test_checkout_single_item(self, page_objects):
        # Sort by price ascending, and add first product listed to cart. Then go to cart
        with allure.step("Products Page steps"):
            page_objects["products_page"].sort_products_by_price_ascending()
            page_objects["products_page"].add_item_to_cart_by_order(0)
            page_objects["site_wide_ui"].click_on_shopping_cart_button()
        with allure.step("Cart Page steps"):
            page_objects["cart_page"].checkout()
        with allure.step("Checkout Stage 1 steps"):
            page_objects["checkout_stage_1"].fill_your_information_form('nate', 'dog', '91210')
        with allure.step("Checkout Stage 2 steps"):
            page_objects["checkout_stage_2"].finish_checkout()
        # After checkout completed, check for order confirmation message

        with allure.step("Order Confirmation steps:"):
            expected_order_confirmation_text = 'your order has been dispatched'
            actual_order_confirmation_text = page_objects[
                "checkout_complete_page"].get_checkout_complete_confirmation_text().lower()
            assert expected_order_confirmation_text in actual_order_confirmation_text, f'Order confirmation not displayed or incorrect: {actual_order_confirmation_text} '

    def test_checkout_multiple_items(self, page_objects):
        # Select product from products page, and add to cart
        page_objects["products_page"].select_item_by_position(0)
        page_objects["product_item_page"].add_item_to_cart()
        page_objects["product_item_page"].back_to_products()

        # Select another product from products page, and add to cart
        page_objects["products_page"].select_item_by_position(1)
        page_objects["product_item_page"].add_item_to_cart()
        page_objects["product_item_page"].back_to_products()

        # Go to cart & checkout
        page_objects["site_wide_ui"].click_on_shopping_cart_button()
        page_objects["cart_page"].checkout()
        page_objects["checkout_stage_1"].fill_your_information_form('nate', 'dog', '91210')
        page_objects["checkout_stage_2"].finish_checkout()

        # After checkout completed, check for order confirmation message
        expected_order_confirmation_text = 'your order has been dispatched'
        actual_order_confirmation_text = page_objects[
            "checkout_complete_page"].get_checkout_complete_confirmation_text().lower()
        assert expected_order_confirmation_text in actual_order_confirmation_text, f'Order confirmation not displayed or incorrect: {actual_order_confirmation_text} '

    def test_cancel_checkout_stage1(self, page_objects):
        # add an item to cart
        page_objects["products_page"].add_item_to_cart_by_order(0)

        # Checkout flow till step 1 [user info]
        page_objects["site_wide_ui"].click_on_shopping_cart_button()
        page_objects["cart_page"].checkout()

        # cancel checkout
        page_objects["checkout_stage_1"].cancel_checkout()

        # Check user is redirected to cart page
        assert page_objects["cart_page"].get_header_title() == 'Your Cart'

    def test_cancel_checkout_stage2(self, page_objects):
        # Add an item to cart
        page_objects["products_page"].add_item_to_cart_by_order(0)

        # Checkout Flow till step 2 [order overview]
        page_objects["site_wide_ui"].click_on_shopping_cart_button()
        page_objects["cart_page"].checkout()
        page_objects["checkout_stage_1"].fill_your_information_form('nate', 'dog', '91210')

        # Cancel checkout
        page_objects["checkout_stage_2"].cancel_checkout()

        # Check user is redirected to products page
        assert page_objects["products_page"].get_header_title() == 'Products'
