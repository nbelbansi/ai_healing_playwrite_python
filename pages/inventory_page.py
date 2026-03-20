from playwright.sync_api import Page
from .BasePage import BasePage

class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._item_prices = page.locator(".inventory_item_price")
        self._cart_badge = page.locator(".shopping_cart_badge")
        self._sort_dropdown = "[data-test='product-sort-container']"

    def sort_by_price_low_to_high(self):
        # Using healing for the dropdown
        self.click_with_healing(self._sort_dropdown, "The product sort dropdown")
        self.page.locator(self._sort_dropdown).select_option("lohi")

    def get_all_prices(self):
        prices_text = self._item_prices.all_inner_texts()
        return [float(p.replace('$', '')) for p in prices_text]

    def add_item_to_cart(self, product_name_id):
        # We pass the selector and a description for the AI
        selector = f"[data-test='add-to-cart-{product_name_id}']"
        description = f"The Add to Cart button for {product_name_id}"

        self.click_with_healing(selector, description)

    def get_cart_count(self):
        return self._cart_badge.inner_text()

    def verify_cart_count(self, expected_count: str):
        actual = self.get_cart_count()
        assert actual == expected_count, f"Expected {expected_count} items, but found {actual}"