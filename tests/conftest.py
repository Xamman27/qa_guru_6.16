import pytest
from selene import browser
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True)
def browser_settings():
    browser.config.base_url = 'https://demoqa.com/'
    driver_options = webdriver.ChromeOptions()
    browser.config.type_by_js = True
    browser.config.driver_options = driver_options
    browser.config.driver = webdriver.Chrome(
        service=ChromeService(executable_path=ChromeDriverManager().install()),
        options=driver_options)
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()
