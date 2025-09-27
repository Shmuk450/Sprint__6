from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Куки
    COOKIE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")

    # Поля ввода
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.CLASS_NAME, "select-search__input")
    METRO_OPTION = (By.CLASS_NAME, "select-search__option")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Кнопка Далее
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Поле даты доставки
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    # Срок аренды
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")

    @staticmethod
    def get_period_option(period_text):
        return By.XPATH, f"//div[@class='Dropdown-option' and text()='{period_text}']"

    # Цвет
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")

    # Комментарий
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Кнопка Заказать
    ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")

    # Подтверждение заказа
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Модальное окно с текстом "Заказ оформлен"
    CONFIRM_MESSAGE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")