import allure
from pages.main_page import MainPage


class TestLogoRedirects:

    @allure.title("Проверка редиректа по клику на логотип Яндекса")
    def test_click_yandex_logo(self, browser):
        main_page = MainPage(browser)
        main_page.open("https://qa-scooter.praktikum-services.ru/")

        # Сначала узнаём текущее количество вкладок
        current_handles_count = len(browser.window_handles)

        # Кликаем по логотипу Яндекса
        main_page.click_yandex_logo()

        # Ждём появления новой вкладки
        main_page.wait_for_new_window(current_handles_count)

        # Переключаемся на новую вкладку (с индексом 1)
        main_page.switch_to_tab(1)

        # Ждём, пока URL новой вкладки будет содержать "dzen.ru"
        main_page.wait_for_url_contains("dzen.ru")

        # Получаем текущий URL новой вкладки
        current_url = main_page.get_current_url()

        # Проверяем, что это действительно редирект на Дзен
        assert "dzen.ru" in current_url

    @allure.title("Проверка редиректа по клику на логотип Самоката")
    def test_click_scooter_logo(self, browser):
        main_page = MainPage(browser)
        main_page.open("https://qa-scooter.praktikum-services.ru/order")

        # Клик по логотипу Самоката
        main_page.click_scooter_logo()

        # Проверка URL после перехода
        current_url = main_page.get_current_url()
        assert current_url == "https://qa-scooter.praktikum-services.ru/"