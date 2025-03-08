from behave import given, when, then
from selenium.webdriver.common.by import By
from features.environment import Context
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the eBay homepage')
def navigate_to_ebay(context: Context):
    context.ebay_category_page.navigate_to_ebay()

@when('I navigate to "{category}" category')
def navigate_to_category(context: Context, category: str):
    context.ebay_category_page.navigate_to_category(category)

@when('I navigate to "{category}" subcategory')
def navigate_to_subcategory(context: Context, category: str):
    context.ebay_category_page.navigate_to_subcategory(category)

@when('I apply the following filters "{filter_type}" with "{filter_value}"')
def apply_filters(context: Context, filter_type: str, filter_value: str):
    filter_button_xpath = f"//button[contains(.,'{filter_type}')]"
    filter_value_xpath = f"//a[contains(.,'{filter_value}')]"
    context.driver.find_element(By.XPATH, filter_button_xpath).click()
    context.driver.find_element(By.XPATH, filter_value_xpath).click()
    print(f"Applied filter: {filter_type} with value: {filter_value}")

@then('I should see all selected "{value}"')
def verify_filters(context: Context, value: str):
    assert context.ebay_category_page.verify_filters_applied(value)

@when('I click on Cell Phones & Smartphones')
def click_smartphones_subcategory(context: Context):
    context.ebay_category_page.click_smartphones_subcategory()

@when('I enter "{search_string}" in the search bar')
def step_when_i_enter_search_string(context: Context, search_string: str):
    context.ebay_search_page.enter_search_string(search_string)

@when('I select "{category}" from the search category')
def step_when_i_select_category(context: Context, category: str):
    context.ebay_search_page.select_category(category)

@then('the first result name should contain "{search_string}"')
def step_then_first_result_should_contain_search_string(context: Context, search_string: str):
    first_result_title = context.ebay_search_page.get_first_result_title()

    assert first_result_title, "No search results found!"
    assert search_string.lower() in first_result_title.lower(), (
        f"Expected '{search_string}' to be in first result title, but got '{first_result_title}'"
    )
