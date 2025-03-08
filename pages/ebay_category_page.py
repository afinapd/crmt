from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage

class EbayCategoryPage(BasePage):
    # Locators
    ELECTRONICS_CATEGORY = (By.XPATH, "//a[contains(text(),'Electronics')]")
    CELL_PHONES_CATEGORY = (By.XPATH, "//a[contains(.,'Cell Phones & Accessories')]")
    SMARTPHONES_SUBCATEGORY = (By.XPATH, "//a[contains(.,'Cell Phones & Smartphones')]")
    ALL_FILTERS_BUTTON = (By.XPATH, "//a[contains(.,'All Listings')]")
    
    # Filter Modal Locators
    CONDITION_FILTER = (By.XPATH, "//div[contains(text(),'Condition')]")
    PRICE_FILTER = (By.XPATH, "//div[contains(text(),'Price')]")
    LOCATION_FILTER = (By.XPATH, "//div[contains(text(),'Item Location')]")
    APPLY_FILTERS_BUTTON = (By.XPATH, "//button[contains(text(),'Apply')]")
    FILTER_APPLIED= (By.XPATH, "//span[@class='filter-label' and contains(text(),'filters applied')]")
    
    def navigate_to_ebay(self):
        self.driver.get("https://www.ebay.com")
        
    def navigate_to_category(self, category_name):
        condition_option = (By.XPATH, f"//a[contains(text(),'{category_name}')]")
        self.find_clickable_element(*condition_option).click()

    def navigate_to_subcategory(self, category_name):
        condition_option = (By.XPATH, f"//a[contains(.,'{category_name}')]")
        self.find_clickable_element(*condition_option).click()
        
    def open_all_filters(self):
        self.find_clickable_element(*self.ALL_FILTERS_BUTTON).click()
        
    def apply_filters(self, condition, price_range, location):
        # Select condition filter
        self.find_clickable_element(*self.CONDITION_FILTER).click()
        condition_option = (By.XPATH, f"//span[contains(text(),'{condition}')]")
        self.find_clickable_element(*condition_option).click()
        
        # Select price filter
        self.find_clickable_element(*self.PRICE_FILTER).click()
        min_price, max_price = price_range.split('-')
        min_price_input = (By.XPATH, "//input[contains(@aria-label,'Minimum Value')]")
        max_price_input = (By.XPATH, "//input[contains(@aria-label,'Maximum Value')]")
        self.find_element(*min_price_input).send_keys(min_price)
        self.find_element(*max_price_input).send_keys(max_price)
        
        # Select location filter
        self.find_clickable_element(*self.LOCATION_FILTER).click()
        location_option = (By.XPATH, f"//span[contains(text(),'{location}')]")
        self.find_clickable_element(*location_option).click()
        
        # Apply filters
        self.find_clickable_element(*self.APPLY_FILTERS_BUTTON).click()
        
    def verify_filters_applied(self, value):
        filter_applied_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FILTER_APPLIED))
        assert value in filter_applied_element.text, f"Expected text '{value}' not found in applied filters."
        return True
        