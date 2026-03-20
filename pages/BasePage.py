# import time
# from playwright.sync_api import Page, TimeoutError
# from utils.ai_healer import AIHealer # Assuming you saved your class in AIHealer.py
#
# class BasePage:
#     def __init__(self, page: Page):
#         self.page = page
#         self.healer = AIHealer()
#
#     def click_with_healing(self, selector: str, description: str):
#         try:
#             # Attempt 1: Standard Playwright Click
#             self.page.wait_for_selector(selector, timeout=5000)
#             self.page.click(selector)
#         except TimeoutError:
#             print(f"\n[AI HEALER] Selector '{selector}' failed. Healing for: {description}...")
#
#             # Get current HTML and ask Groq for a new selector
#             html = self.page.content()
#             new_selector = self.healer.suggest_new_selector(html, description)
#
#             if new_selector:
#                 print(f"[AI HEALER] Suggested New Selector: {new_selector}")
#                 # Attempt 2: Use the AI suggested selector
#                 self.page.click(new_selector)
#             else:
#                 raise Exception(f"Self-healing failed for {description}")
#
#     def fill_with_healing(self, selector: str, text: str, description: str):
#         try:
#             self.page.wait_for_selector(selector, timeout=5000)
#             self.page.fill(selector, text)
#         except TimeoutError:
#             print(f"\n[AI HEALER] Selector '{selector}' failed. Healing for: {description}...")
#             html = self.page.content()
#             new_selector = self.healer.suggest_new_selector(html, description)
#             if new_selector:
#                 self.page.fill(new_selector, text)
#             else:
#                 raise Exception(f"Self-healing failed for {description}")

import time
import os
from playwright.sync_api import Page, TimeoutError
from utils.ai_healer import AIHealer

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.healer = AIHealer()
        # Ensure a directory exists for healing evidence
        if not os.path.exists("healing_evidence"):
            os.makedirs("healing_evidence")

    def _capture_healing_evidence(self, description: str, old_selector: str, new_selector: str):
        """Captures a screenshot of the moment AI saved the test."""
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        file_path = f"healing_evidence/healed_{timestamp}.png"
        self.page.screenshot(path=file_path)
        print(f"✨ [AI SUCCESS] Healed '{description}'")
        print(f"   - Failed: {old_selector}")
        print(f"   - Fixed with: {new_selector}")
        print(f"   - Evidence saved to: {file_path}")

    def click_with_healing(self, selector: str, description: str):
        try:
            self.page.wait_for_selector(selector, timeout=5000)
            self.page.click(selector)
        except TimeoutError:
            print(f"\n[AI HEALER] Selector '{selector}' failed. Healing for: {description}...")

            html = self.page.content()
            new_selector = self.healer.suggest_new_selector(html, description)

            if new_selector:
                self._capture_healing_evidence(description, selector, new_selector)
                self.page.click(new_selector)
            else:
                raise Exception(f"Self-healing failed for {description}")

    def fill_with_healing(self, selector: str, text: str, description: str):
        try:
            self.page.wait_for_selector(selector, timeout=5000)
            self.page.fill(selector, text)
        except TimeoutError:
            print(f"\n[AI HEALER] Selector '{selector}' failed. Healing for: {description}...")

            html = self.page.content()
            new_selector = self.healer.suggest_new_selector(html, description)

            if new_selector:
                self._capture_healing_evidence(description, selector, new_selector)
                self.page.fill(new_selector, text)
            else:
                raise Exception(f"Self-healing failed for {description}")