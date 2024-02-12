
class TestCart:

    def test_remove_item_from_cart(self, page_objects):
        # Add product to cart
        page_objects["products_page"].add_item_to_cart_by_order(0)

        # Go to cart, and remove item
        page_objects["site_wide_ui"].click_on_shopping_cart_button()
        page_objects["cart_page"].remove_cart_item(0)

        # Check cart is empty of items
        assert page_objects["cart_page"].get_number_items_in_cart() == 0, "Number of items in cart should be zero."

    def test_remove_all_cart_items(self, page_objects):
        # Add all items in products page to cart
        page_objects["products_page"].add_all_page_items_to_cart()

        # Go to cart, and remove all items in cart
        page_objects["site_wide_ui"].click_on_shopping_cart_button()
        page_objects["cart_page"].remove_all_cart_items()

        # Check cart is empty of items
        assert page_objects["cart_page"].get_number_items_in_cart() == 0, "Number of items in cart should be zero."

    def test_cart_badge_counter_increases_on_adding_item(self, page_objects):
        # Add a single item to cart
        page_objects["products_page"].add_item_to_cart_by_order(0)

        # Check cart badge counter increments to 1
        badgeCounter = page_objects["site_wide_ui"].get_shopping_cart_badge_counter()
        assert badgeCounter == 1, f"Cart counter has incorrect value. Expected: 1, Actual: {badgeCounter}"

    def test_cart_badge_counter_decreases_on_removing_item(self, page_objects):
        # Add 2 items to cart
        page_objects["products_page"].add_item_to_cart_by_order(0)
        page_objects["products_page"].add_item_to_cart_by_order(1)

        # Go to cart, and check badge counter [should be 2]
        page_objects["site_wide_ui"].click_on_shopping_cart_button()
        badgeCounterPre = page_objects["site_wide_ui"].get_shopping_cart_badge_counter()

        # Remove one item from cart
        page_objects["cart_page"].remove_cart_item(0)
        badgeCounterPost = page_objects["site_wide_ui"].get_shopping_cart_badge_counter()

        # Check badge counter decreased by 1 after removing item
        assert (badgeCounterPre - badgeCounterPost == 1), f"Cart counter did not decrease on removing item. Expected: 1, Actual: {badgeCounterPost}"
