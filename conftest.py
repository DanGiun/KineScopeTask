import os
from typing import Generator

import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import SubRequest
from playwright.sync_api import Browser, BrowserType, Page
from playwright.sync_api import sync_playwright
from playwright.sync_api import Playwright, APIRequestContext

PROJECT_ROOT: str = os.path.dirname(os.path.abspath(__file__))
# KINE_API_TOKEN = '25e64257-db0f-4bca-a364-1c2aca33146e'
# PARENT_ID = ''
# X_Video_Title = ''
# X_Video_URL = ''


def pytest_addoption(parser: Parser) -> None:
    """
    Парсер ожидаемых аргументов для Pytest.

    Args:
        parser (Parser): Объект парсера аргументов Pytest.
    """
    parser.addoption(
        '--browser',
        action='store',
        default='chromium',
        help="""Available browsers: Google Chrome(chromium), Yandex Browser(yandex), Safari(safari), 
        Microsoft Edge(edge). Default value - chromium""",
    )
    parser.addoption(
        '--headless',
        action='store_true',
        help='Browser will be in headless mode if pass this argument',
    )


# @pytest.fixture(scope="session")
# def api_request_context(
#         playwright: Playwright,
# ) -> Generator[APIRequestContext, None, None]:
#     headers = {
#         "Authorization": f"Bearer {KINE_API_TOKEN}",
#         "X-Parent-ID": f"{PARENT_ID}",
#         "X-Video-Title": f"{X_Video_Title}",
#         "X-Video-URL": f"{X_Video_URL}",
#     }
#     request_context = playwright.request.new_context(
#         base_url="https://uploader.kinescope.io/v2/video", extra_http_headers=headers
#     )
#     yield request_context
#     request_context.dispose()


@pytest.fixture(scope='function', autouse=False)
def start_browser(request: SubRequest) -> BrowserType:
    """
    Фикстура для запуска браузера (BrowserType) в зависимости от аргумента --browser.

    Args:
        request (SubRequest): Запрос на использование фикстуры.

    Yields:
        BrowserType: Тип браузера для запуска (Chromium, WebKit, или Edge).
    """
    browser = request.config.getoption('--browser')
    with sync_playwright() as pw:
        if browser == 'safari':
            yield pw.webkit
        else:  # For chromium, yandex, and edge. Because all of them have Chrome as their core
            yield pw.chromium


@pytest.fixture(scope='function', autouse=False)
def browser(request: SubRequest, start_browser: BrowserType) -> Browser:
    """
    Фикстура для создания экземпляра браузера (Browser) в зависимости от аргументов --browser и --headless.

    Args:
        request (SubRequest): Запрос на использование фикстуры.
        start_browser (BrowserType): Тип браузера, полученный из предыдущей фикстуры.

    Yields:
        Browser: Экземпляр браузера для использования в тестах.
    """
    headless = request.config.getoption('--headless', False)
    browser = request.config.getoption('--browser')
    if browser != 'chromium':
        raise RuntimeError('Yandex Browser, Safari, and Microsoft Edge were not configured')
    browser = start_browser.launch(headless=headless)
    yield browser
    browser.close()


@pytest.fixture(scope='function', autouse=False)
def page(browser: Browser) -> Page:
    """
    Фикстура для создания экземпляра веб-страницы (Page) внутри браузера.

    Args:
        browser (Browser): Экземпляр браузера, полученный из предыдущей фикстуры.

    Yields:
        Page: Экземпляр веб-страницы для использования в тестах.
    """
    page = browser.new_page()
    yield page
    page.close()
