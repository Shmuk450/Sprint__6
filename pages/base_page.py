import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.driver.implicitly_wait(10)

    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент: {locator}")
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Найти все элементы: {locator}")
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Проскроллить к элементу")
    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента: {locator}")
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидание открытия новой вкладки")
    def wait_for_new_tab_opened(self, expected_tabs_count):
        self.wait.until(lambda d: len(d.window_handles) >= expected_tabs_count)

    @allure.step("Переключение на вкладку с индексом: {index}")
    def switch_to_tab(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step("Ожидание, пока URL будет содержать: {text}")
    def wait_for_url_contains(self, text):
        self.wait.until(lambda d: text in d.current_url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Клик по элементу через JavaScript")
    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ожидание открытия новой вкладки (ожидание увеличения количества вкладок)")
    def wait_for_new_window(self, previous_handles_count):
        self.wait.until(lambda driver: len(driver.window_handles) > previous_handles_count)  
