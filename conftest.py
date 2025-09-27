import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="function")
def browser():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1920, 1080) 
    yield driver
    driver.quit()