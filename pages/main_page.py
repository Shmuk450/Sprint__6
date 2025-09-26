from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def click_order_button_header(self):
        self.driver.find_element(By.CLASS_NAME, "Button_Button__ra12g").click()

    def scroll_to_order_button_footer(self):
        order_button = self.driver.find_elements(By.CLASS_NAME, "Button_Button__ra12g")[-1]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_button)

    def click_order_button_footer(self):
        self.driver.find_elements(By.CLASS_NAME, "Button_Button__ra12g")[-1].click()

    def click_scooter_logo(self):
        self.driver.find_element(By.CLASS_NAME, "Header_LogoScooter__3lsAR").click()

    def click_yandex_logo(self):
        self.driver.find_element(By.CLASS_NAME, "Header_LogoYandex__3TSOI").click()

    def scroll_to_question(self, index):
        element = self.driver.find_elements(By.CLASS_NAME, "accordion__button")[index]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click_question(self, index):
        element = self.driver.find_elements(By.CLASS_NAME, "accordion__button")[index]
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "accordion__button")))
        self.driver.execute_script("arguments[0].click();", element)

    def get_answer_text(self, index):
        panel_locator = (By.ID, f"accordion__panel-{index}")
        self.wait.until(EC.visibility_of_element_located(panel_locator))
        return self.driver.find_element(*panel_locator).text