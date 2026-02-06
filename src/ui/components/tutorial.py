from .base_component import BaseComponent

from playwright.async_api import Page, Locator, expect

class Tutorial(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.tutorial_popup = self._page.locator("xpath=/html/body/div/div[2]/div")
        self.next_button = self._page.get_by_text("Next")
    
    async def click_next_button(self):
        await self.next_button.click()