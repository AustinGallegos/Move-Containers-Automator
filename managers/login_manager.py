import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def sign_in(driver):
    """Sign in to FCLM Portal."""
    driver.get(os.getenv("PORTAL_LINK"))
    _handle_badge(driver)
    _handle_password(driver)
    _handle_warehouse(driver)


def _handle_badge(driver):
    """Enters badge information on the FCLM Portal."""
    badge_input = driver.find_element(By.ID, "badgeBarcodeId")
    badge_input.click()
    badge_input.send_keys(os.getenv("BADGE"))
    badge_input.send_keys(Keys.ENTER)


def _handle_password(driver):
    """Enters password information on the FCLM Portal."""
    password_input = driver.find_element(By.ID, "password")
    password_input.click()
    password_input.send_keys(os.getenv("PASSWORD"))
    password_input.send_keys(Keys.ENTER)


def _handle_warehouse(driver):
    """Enters the warehouse information on the FCLM Portal."""
    warehouse_input = driver.find_element(By.ID, "qlInput")
    warehouse_input.click()
    warehouse_input.send_keys("SMF9")
    warehouse_input.send_keys(Keys.ENTER)
