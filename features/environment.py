from behave.runner import Context as BehaveContext
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from pages.ebay_category_page import EbayCategoryPage
from pages.ebay_search_page import EbaySearchPage

class Context(BehaveContext):
    driver: WebDriver
    ebay_category_page: EbayCategoryPage
    ebay_search_page: EbaySearchPage
    delay: float

def before_all(context: Context):
    context.delay = float(context.config.userdata.get('DELAY', '0'))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')

    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()

    # Initialize page objects
    context.ebay_category_page = EbayCategoryPage(context.driver)
    context.ebay_search_page = EbaySearchPage(context.driver)

# def after_all(context: Context):
    # context.driver.quit()
