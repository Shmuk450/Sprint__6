from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_success_message_present(self):
        # Ждём, пока появится заголовок модалки
        success_header = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "Order_ModalHeader__3FDaJ"))
        )
        return "Заказ оформлен" in success_header.text