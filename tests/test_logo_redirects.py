import time
import allure 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


def test_click_yandex_logo(browser):
    main_page = MainPage(browser)
    main_page.open("https://qa-scooter.praktikum-services.ru/")
    main_page.click_yandex_logo()

    # Ожидание появления второй вкладки
    WebDriverWait(browser, 10).until(lambda d: len(d.window_handles) > 1)

    # Переключаемся на новую вкладку
    browser.switch_to.window(browser.window_handles[1])

    # Явное ожидание, пока в URL появится 'dzen.ru'
    WebDriverWait(browser, 10).until(lambda d: "dzen.ru" in d.current_url)

    current_url = browser.current_url
    print("🔎 URL новой вкладки:", current_url)

    assert "dzen.ru" in current_url


def test_click_scooter_logo(browser):
    main_page = MainPage(browser)
    main_page.open("https://qa-scooter.praktikum-services.ru/order")
    main_page.click_scooter_logo()
    assert browser.current_url == "https://qa-scooter.praktikum-services.ru/"