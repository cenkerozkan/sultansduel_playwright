import asyncio
from random import randint
from collections import OrderedDict

import pytest

from src.ui.pages.login_page import LoginPage
from src.ui.components.tutorial import Tutorial
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_create_account(
    page: Page,
    env: OrderedDict,
    random_email: str,
    password: str
):
    await page.goto(env["BASE_URL"], wait_until="networkidle")
    
    login_page = LoginPage(page)
    # NOTE: Why use networkidle? some websites require more than one network 
    #       activities to load all components. Without waiting properly,
    #       tests can become flaky.
    await login_page.click_create_account_link()
    # await asyncio.sleep(5000)

    await expect(login_page.email_box).to_be_visible()
    await expect(login_page.password_box).to_be_visible()
    await expect(login_page.confirm_password_box).to_be_visible()

    await login_page.register(
        random_email,
        password,
        password
    )
    await login_page.create_account_button.click()

    # Now how can we be sure about if the
    tutorial_component = Tutorial(page)

    # What could be the other way instead of this? (wait for response?)
    await expect(tutorial_component.tutorial_popup).to_be_visible()
