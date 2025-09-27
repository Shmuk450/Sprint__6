import allure
from pages.base_page import BasePage
from locators.confirmation_page_locators import ConfirmationPageLocators


class ConfirmationPage(BasePage):

    @allure.step("Проверить наличие сообщения об успешном заказе")
    def is_success_message_present(self):
        success_header = self.wait_for_visibility(ConfirmationPageLocators.SUCCESS_HEADER)
        return "Заказ оформлен" in success_header.text