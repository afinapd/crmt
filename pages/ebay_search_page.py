from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class EbaySearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.ID, "gh-ac")
        self.category_dropdown = (By.ID, "gh-cat")
        self.search_button = (By.XPATH, "//button[contains(@class, 'gh-search-button')]")
        self.first_result_title = (By.XPATH, "//a[@class='s-item__link']//span[@class='BOLD']")

    def enter_search_string(self, search_string):
        search_bar_element = self.driver.find_element(*self.search_bar)
        search_bar_element.clear()
        search_bar_element.send_keys(search_string)
        self.driver.find_element(*self.search_button).click()

    def select_category(self, category):
        category_dropdown_element = self.driver.find_element(*self.category_dropdown)
        category_dropdown_element.send_keys(category)

    def get_first_result_title(self):
        return self.driver.find_element(*self.first_result_title).text