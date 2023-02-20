import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru", help="Enter language: ru, en, es, etc")

@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': request.config.getoption("language")})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(20)
    yield browser
    print("\nquit browser..")
    browser.quit()
