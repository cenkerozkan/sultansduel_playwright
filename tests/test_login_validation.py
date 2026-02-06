import asyncio
from random import randint
from collections import OrderedDict

import pytest

from src.ui.pages.login_page import LoginPage
from src.ui.components.tutorial import Tutorial
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_login_validation(
    page: Page,
    env: OrderedDict,
    random_email: str,
    password: str
):
    await page.goto(env["BASE_URL"], wait_until="networkidle")

    login_page = LoginPage(page)

    await login_page.login(random_email, password)

    await expect(login_page.auth_failed_message).to_be_visible()