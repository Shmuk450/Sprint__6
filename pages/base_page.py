class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)  
    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def is_element_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()