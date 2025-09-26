from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def accept_cookies(self):
        try:
            button = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='да все привыкли']")))
            button.click()
        except:
            pass 

    def fill_personal_info(self, name, surname, address, metro, phone):
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Имя']").send_keys(name)
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Фамилия']").send_keys(surname)
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']").send_keys(address)

        # Станция метро
        self.driver.find_element(By.CLASS_NAME, "select-search__input").send_keys(metro)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "select-search__option"))).click()

        self.driver.find_element(By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']").send_keys(phone)

    def click_next(self):
        self.driver.find_element(By.XPATH, "//button[text()='Далее']").click()

    def fill_rent_info(self, date, period, color, comment):
        # Ввод даты с прокруткой
        date_input = self.driver.find_element(By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", date_input)
        # Нажимаем на поле, чтобы открыть календарь
        date_input.click()
        # Вводим дату и подтверждаем
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

        # Открытие выпадающего списка срока аренды
        period_dropdown = self.driver.find_element(By.CLASS_NAME, "Dropdown-placeholder")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", period_dropdown)
        period_dropdown.click()

        # Ожидание и выбор нужного периода
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']"))).click()

        # Выбор цвета
        if color.lower() == "чёрный жемчуг":
            self.driver.find_element(By.ID, "black").click()
        elif color.lower() == "серая безысходность":
            self.driver.find_element(By.ID, "grey").click()

        # Ввод комментария
        self.driver.find_element(By.XPATH, "//input[@placeholder='Комментарий для курьера']").send_keys(comment)

    def click_order(self):
        try:
            # Более точный XPath для нижней кнопки
            button = self.driver.find_element(By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")))

            button.click()

        except Exception as e:
            raise

    def confirm_order(self):
        try:
            confirm_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Да']")))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", confirm_button)
            confirm_button.click()

        except Exception as e:
            raise
    def confirm_order(self):
        try:
            confirm_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Да']")))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", confirm_button)
            confirm_button.click()
        except Exception as e:
            raise
