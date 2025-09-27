import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.confirmation_page import ConfirmationPage


class TestOrder:

    @allure.title("Создание заказа через кнопку в хедере")
    def test_create_order_from_header(self, browser):
        main_page = MainPage(browser)
        order_page = OrderPage(browser)
        confirmation_page = ConfirmationPage(browser)

        main_page.open("https://qa-scooter.praktikum-services.ru/")
        main_page.click_order_button_header()

        order_page.accept_cookies()
        order_page.fill_personal_info(
            name="Анна",
            surname="Тестова",
            address="Москва, Тверская 1",
            metro="Черкизовская",
            phone="+79991112233"
        )
        order_page.click_next()
        order_page.fill_rent_info(
            date="25.10.2025",
            period="двое суток",
            color="чёрный жемчуг",
            comment="Тестовый заказ"
        )
        order_page.click_order()
        order_page.confirm_order()

        assert confirmation_page.is_success_message_present()

    @allure.title("Создание заказа через кнопку в футере")
    def test_create_order_from_footer(self, browser):
        main_page = MainPage(browser)
        order_page = OrderPage(browser)
        confirmation_page = ConfirmationPage(browser)

        main_page.open("https://qa-scooter.praktikum-services.ru/")
        main_page.scroll_to_order_button_footer()
        main_page.click_order_button_footer()

        order_page.accept_cookies()
        order_page.fill_personal_info(
            name="Анна",
            surname="Тестова",
            address="Москва, Тверская 1",
            metro="Черкизовская",
            phone="+79991112233"
        )
        order_page.click_next()
        order_page.fill_rent_info(
            date="25.10.2025",
            period="двое суток",
            color="чёрный жемчуг",
            comment="Тестовый заказ"
        )
        order_page.click_order()
        order_page.confirm_order()

        assert confirmation_page.is_success_message_present()