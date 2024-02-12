from tests.cart_tests import CartTests
from tests.checkout_tests import CheckoutTests
from tests.login_tests import LoginTests
from tests.products_page_tests import ProductsPageTests


def runTests_v1():
    LoginTests.login_standard_user()
    CheckoutTests.checkout_items()
    CheckoutTests.checkout_cheapest_item()
    CheckoutTests.cancel_checkout_stage1()
    CheckoutTests.cancel_checkout_stage2()
    ProductsPageTests.sort_products()
    CartTests.remove_item_from_cart()
    CartTests.remove_all_cart_items()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runTests_v1()
