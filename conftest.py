import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def t_config():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

