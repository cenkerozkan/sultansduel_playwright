import asyncio

from playwright.async_api import Page, Locator, expect, Playwright, async_playwright

from .base_component import BaseComponent


class Navbar(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # NOTE: One of these can be re-written with built in in order to show strict violation,
        # especially with get_by_text usage. Trying to locate Decks button with get_by_text causes
        # a "strict mode violation" error since there are multiple matches.
        self.top_link = self._page.get_by_role("link", name="Sultan's Duel")
        self.home_link = self._page.locator(
            "xpath=/html/body/div/nav/div/div[5]/div/div/div[1]/a"
        )
        self.play_link = self._page.locator(
            "xpath=/html/body/div/nav/div/div[5]/div/div/div[2]/a"
        )
        self.decks_link = self._page.locator(
            "xpath=/html/body/div/nav/div/div[5]/div/div/div[3]/a"
        )
        self.games_link = self._page.locator(
            "xpath=/html/body/div/nav/div/div[5]/div/div/div[4]/a"
        )
        self.leaderboard_link = self._page.locator(
            "xpath=/html/body/div/nav/div/div[5]/div/div/div[5]/a"
        )
        self.gameplay_link = self._page.locator(
            "xpath=/html/body/div/nav/div/div[5]/div/div/div[6]/a"
        )
        self.tutorial_button = self._page.get_by_text("Tutorial")
        self.theme_button = self._page.get_by_role("button", name="Change Theme")
        self.logout_button = self._page.get_by_role("button", name="Logout")
    
    @classmethod
    def create(cls, page: Page) -> "Navbar":
        navbar = cls(page)
        return navbar

    async def navigate_to_home(self) -> None:
        await self.home_link.click()

    async def navigate_to_play(self) -> None:
        await self.play_link.click()

    async def navigate_to_decks(self) -> None:
        await self.decks_link.click()

    async def navigate_to_games(self) -> None:
        await self.games_link.click()

    async def navigate_to_leaderboard(self) -> None:
        await self.leaderboard_link.click()

    async def navigate_to_gameplay(self) -> None:
        await self.gameplay_link.click()

    async def open_tutorial(self) -> None:
        await self.tutorial_button.click()

    async def toggle_theme(self) -> None:
        await self.theme_button.click()

    async def logout(self) -> None:
        await self.logout_button.click()
