
class TestProductsPage:

    def test_sort_products_by_price_high_low(self, page_objects):
        page_objects["products_page"].sort_products_by_price_descending()
        is_sort_by_price_descending = page_objects["products_page"].validate_correct_ordering_by_price_high_low()
        assert is_sort_by_price_descending, f"Products are not sorted correctly by price descending: {page_objects["products_page"].get_products_prices()}"

    def test_sort_products_by_price_low_high(self, page_objects):
        page_objects["products_page"].sort_products_by_price_ascending()
        is_sort_by_price_ascending = page_objects["products_page"].validate_correct_ordering_by_price_low_high()
        assert is_sort_by_price_ascending, f"Products are not sorted correctly by price ascending: {page_objects["products_page"].get_products_prices()}"

    def test_sort_products_by_name_a_to_z(self, page_objects):
        page_objects["products_page"].sort_products_by_name_ascending()
        is_sort_by_name_ascending = page_objects["products_page"].validate_correct_ordering_by_name_a_z()
        assert is_sort_by_name_ascending, f"Products are not sorted correctly by name ascending: {page_objects["products_page"].get_products_item_names()}"

    def test_sort_products_by_name_z_to_a(self, page_objects):
        page_objects["products_page"].sort_products_by_name_descending()
        is_sort_by_name_descending = page_objects["products_page"].validate_correct_ordering_by_name_z_a()
        assert is_sort_by_name_descending, f"Products are not sorted correctly by name descending: {page_objects["products_page"].get_products_item_names()}"

