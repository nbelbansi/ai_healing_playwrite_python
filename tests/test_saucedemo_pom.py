from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_price_sorting_logic(browser_context):
    # Step 1: Initialize the Page and POMs
    page = browser_context.new_page()
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.navigate()
    login.login_as_standard_user()

    inventory.sort_by_price_low_to_high()
    prices = inventory.get_all_prices()

    assert prices == sorted(prices), f"Prices were not sorted correctly! {prices}"

def test_add_backpack_to_cart(browser_context):
    page = browser_context.new_page()
    login = LoginPage(page)
    inventory = InventoryPage(page)

    # 1. Navigate and Login (Healable)
    login.navigate()
    login.login_as_standard_user()

    # 2. Add to cart (Healable)
    inventory.add_item_to_cart("sauce-labs-backpack")

    # 3. Assert
    inventory.verify_cart_count("1")