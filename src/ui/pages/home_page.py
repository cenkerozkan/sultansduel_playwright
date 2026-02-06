from playwright.async_api import Page, expect, Locator

from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self._new_game_button = page.get_by_text("New Game")
        self._manage_decks_button = page.get_by_text("Manage Decks")
        self._active_games_table = page.get_by_role("table")
        self._top_players_table_header = page.get_by_text("Top Players")
        self._top_players_table = page.get_by_role("table") # Not checked. Maybe we can count?

        async def click_new_game(self) -> None:
            await self._new_game_button.click()
        
        async def click_manage_decks(self) -> None:
            await self._manage_decks_button.click()