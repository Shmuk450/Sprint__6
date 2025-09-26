import pytest
import allure 
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.confirmation_page import ConfirmationPage


@pytest.mark.parametrize("button", ["header", "footer"])
def test_create_order_success(browser, button):
    main_page = MainPage(browser)
    order_page = OrderPage(browser)
    confirmation_page = ConfirmationPage(browser)

    # 1. Открыть главную и нажать нужную кнопку
    main_page.open("https://qa-scooter.praktikum-services.ru/")
    if button == "header":
        main_page.click_order_button_header()
    else:
        main_page.scroll_to_order_button_footer()
        main_page.click_order_button_footer()
    
    order_page.accept_cookies()

    # 2. Заполнение первой части формы
    order_page.fill_personal_info(
        name="Анна",
        surname="Тестова",
        address="Москва, Тверская 1",
        metro="Черкизовская",
        phone="+79991112233"
    )
    order_page.click_next()

    # 3. Заполнение второй части формы
    order_page.fill_rent_info(
        date="25.10.2025",
        period="двое суток",
        color="чёрный жемчуг",
        comment="Тестовый заказ"
    )
    order_page.click_order()
    print("Нажали 'Заказать'")
    order_page.confirm_order()
    print("Нажали 'Да'")

    # 4. Проверка страницы подтверждения
    assert confirmation_page.is_success_message_present()