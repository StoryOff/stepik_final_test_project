import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en etc.")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language is not None:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        print("\nstart chrome browser for test..")
    else:
        raise pytest.UsageError("--language should have correct locale code")
    yield browser
    print("\nquit browser..")
    browser.quit()