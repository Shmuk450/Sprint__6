import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as Loc


class OrderPage(BasePage):

    @allure.step("Принять куки (если отображаются)")
    def accept_cookies(self):
        try:
            button = self.wait_for_clickable(Loc.COOKIE_BUTTON)
            button.click()
        except:
            pass

    @allure.step("Заполнить личные данные: {name}, {surname}, {address}, {metro}, {phone}")
    def fill_personal_info(self, name, surname, address, metro, phone):
        self.find(Loc.FIRST_NAME).send_keys(name)
        self.find(Loc.LAST_NAME).send_keys(surname)
        self.find(Loc.ADDRESS).send_keys(address)
        self.find(Loc.METRO_FIELD).send_keys(metro)
        self.wait_for_clickable(Loc.METRO_OPTION).click()
        self.find(Loc.PHONE).send_keys(phone)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next(self):
        self.find(Loc.NEXT_BUTTON).click()

    @allure.step("Заполнить данные аренды: {date}, {period}, {color}, {comment}")
    def fill_rent_info(self, date, period, color, comment):
        date_input = self.find(Loc.DATE)
        self.scroll_to(date_input)
        date_input.click()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

        dropdown = self.find(Loc.RENT_DROPDOWN)
        self.scroll_to(dropdown)
        dropdown.click()
        option_locator = (Loc.get_period_option(period))
        self.wait_for_clickable(option_locator).click()

        if color.lower() == "чёрный жемчуг":
            self.find(Loc.COLOR_BLACK).click()
        elif color.lower() == "серая безысходность":
            self.find(Loc.COLOR_GREY).click()

        self.find(Loc.COMMENT).send_keys(comment)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order(self):
        button = self.find(Loc.ORDER_BUTTON)
        self.scroll_to(button)
        self.wait_for_clickable(Loc.ORDER_BUTTON)
        button.click()

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        confirm_button = self.wait_for_clickable(Loc.YES_BUTTON)
        self.scroll_to(confirm_button)
        confirm_button.click()