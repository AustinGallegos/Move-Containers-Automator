from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def setup_driver():
    """Set up selenium webdriver for Chrome."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    return driver, wait
