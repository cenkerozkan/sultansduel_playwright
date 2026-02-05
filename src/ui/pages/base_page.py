from playwright.async_api import Page

class BasePage:
    def __init__(self, page: Page, base_url: str):
        self._page = page
        self._base_url = base_url
    
    @property
    def page(self) -> Page:
        return self._page

    @property
    def base_url(self) -> str:
        return self._base_url