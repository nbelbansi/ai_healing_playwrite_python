import time
import logging
import os
from playwright.sync_api import Page, TimeoutError
from utils.ai_healer import AIHealer

logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.healer = AIHealer()
        # Ensure a directory exists for healing evidence
        if not os.path.exists("healing_evidence"):
            os.makedirs("healing_evidence")

    # def _capture_healing_evidence(self, description: str, old_selector: str, new_selector: str):
    #     """Captures a screenshot of the moment AI saved the test."""
    #     timestamp = time.strftime("%Y%m%d-%H%M%S")
    #     file_path = f"healing_evidence/healed_{timestamp}.png"
    #     self.page.screenshot(path=file_path)
    #     print(f"✨ [AI SUCCESS] Healed '{description}'")
    #     print(f"   - Failed: {old_selector}")
    #     print(f"   - Fixed with: {new_selector}")
    #     print(f"   - Evidence saved to: {file_path}")
    def _capture_healing_evidence(self, description: str, old_selector: str, new_selector: str):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        file_path = f"healing_evidence/healed_{timestamp}.png"
        self.page.screenshot(path=file_path)
        logger.info("✨ [AI SUCCESS] Healed '%s'", description)
        logger.info("   - Failed: %s", old_selector)
        logger.info("   - Fixed with: %s", new_selector)
        logger.info("   - Evidence saved to: %s", file_path)

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