from .base_page import BasePage

from playwright.async_api import Page, expect, Locator


class DecksPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self._header = page.get_by_text("My Decks", exact=False)
        # First deck elements
        self._first_deck_name = page.locator("xpath=/html/body/div/main/div/div/div[2]/div[1]/div/div/h3")
        self._first_deck_edit_button = page.locator("xpath=/html/body/div/main/div/div/div[2]/div[1]/div/div[2]/a/button")
        self._first_deck_delete_button = page.locator("xpath=/html/body/div/main/div/div/div[2]/div[1]/div/div[2]/button")

        # Second deck elements
        self._second_deck_name = page.locator("xpath=/html/body/div/main/div/div/div[2]/div[2]/div/div/h3")
        self._second_deck_name_edit_button = page.locator("xpath=/html/body/div/main/div/div/div[2]/div[2]/div/div[2]/a/button")
        self._second_deck_delete_button = page.locator("xpath=/html/body/div/main/div/div/div[2]/div[2]/div/div[2]/button")

        # Third deck elements
        self._third_deck_name = page.locator("xpath=/html/body/div/main/div/div/div[2]/div[3]/div/div/h3")
        self._third_deck_name_edit_button = page.locator("xpath=/html/body/div/main/div/div/div[2]/div[3]/div/div[2]/a/button")
        self._third_deck_delete_button = page.locator("xpath=/html/body/div/main/div/div/div[2]/div[3]/div/div[2]/button")


        async def click_first_deck_edit(self) -> None:
            await self._first_deck_edit_button.click()

        async def click_first_deck_delete(self) -> None:
            await self._first_deck_delete_button.click()

        async def click_second_deck_edit(self) -> None:
            await self._second_deck_name_edit_button.click()

        async def click_second_deck_delete(self) -> None:
            await self._second_deck_delete_button.click()

        async def click_third_deck_edit(self) -> None:
            await self._third_deck_name_edit_button.click()

        async def click_third_deck_delete(self) -> None:    
            await self._third_deck_delete_button.click()