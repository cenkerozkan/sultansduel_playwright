import asyncio

from playwright.async_api import Locator, expect, Playwright, async_playwright

from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page, base_url) -> None:
        super().__init__(page, base_url)

        # Locators
        self.email_box = self._page.get_by_placeholder(text="Email address")
        self.password_box = self._page.get_by_placeholder(text="Password")
        self.confirm_password_box = self._page.get_by_placeholder(
            text="Confirm Password"
        )
        self.forgot_password_link = self._page.get_by_role(
            role="link", name="Forgot password?"
        )
        self.create_account_link = self._page.get_by_role(
            role="link", name="Create account"
        )
        self.login_link = self._page.get_by_role(role="link", name="Login")

    async def fill_email(self, value: str):
        await self.email_box.fill(value=value)

    async def fill_password(self, value: str):
        await self.password_box.fill(value=value)

    async def fill_confirm_password(self, value: str):
        await self.confirm_password_box.fill(value=value)

    async def click_forgot_password(self):
        await self.forgot_password_link.click()

    async def click_create_account(self):
        await self.create_account_link.click()

    async def click_login(self):
        await self.login_link.click()
