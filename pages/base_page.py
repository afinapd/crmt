from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def find_clickable_element(self, by, value):
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def is_url_matches(self, url_pattern):
        return url_pattern in self.driver.current_url
