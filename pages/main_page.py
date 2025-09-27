import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_order_button_header(self):
        self.find(MainPageLocators.ORDER_BUTTON_TOP).click()

    @allure.step("Проскроллить до нижней кнопки 'Заказать'")
    def scroll_to_order_button_footer(self):
        self.scroll_to(self.find(MainPageLocators.ORDER_BUTTON_BOTTOM))

    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_order_button_footer(self):
        self.find(MainPageLocators.ORDER_BUTTON_BOTTOM).click()

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.find(MainPageLocators.SCOOTER_LOGO).click()

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.find(MainPageLocators.YANDEX_LOGO).click()

    @allure.step("Проскроллить до вопроса с индексом: {index}")
    def scroll_to_question(self, index):
        locator = MainPageLocators.QUESTION_SELECTORS[index]
        self.scroll_to(self.find(locator))

    @allure.step("Клик по вопросу с индексом: {index}")
    def click_question(self, index):
        locator = MainPageLocators.QUESTION_SELECTORS[index]
        element = self.find(locator)
        self.scroll_to(element)
        self.wait_for_clickable(locator)
        self.js_click(element)  

    @allure.step("Получить текст ответа на вопрос с индексом: {index}")
    def get_answer_text(self, index):
        locator = MainPageLocators.ANSWER_SELECTORS[index]
        self.wait_for_visibility(locator)
        return self.find(locator).text