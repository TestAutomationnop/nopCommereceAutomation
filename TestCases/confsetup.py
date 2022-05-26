import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture(scope="package")
def web_setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver
