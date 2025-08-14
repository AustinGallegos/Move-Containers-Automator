import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.interfaces import LoginHandlerInterface


class FCLMSignIn(LoginHandlerInterface):
    def __init__(self):
        self.driver = None

    def sign_in(self, driver):
        """Sign in to FCLM Portal."""
        self.driver = driver
        self.driver.get(os.getenv("PORTAL_LINK"))
        self.handle_badge()
        self.handle_password()
        self.handle_warehouse()

    def handle_badge(self):
        """Enters badge information on the FCLM Portal."""
        badge_input = self.driver.find_element(By.ID, "badgeBarcodeId")
        badge_input.click()
        badge_input.send_keys(os.getenv("BADGE"))
        badge_input.send_keys(Keys.ENTER)

    def handle_password(self):
        """Enters password information on the FCLM Portal."""
        password_input = self.driver.find_element(By.ID, "password")
        password_input.click()
        password_input.send_keys(os.getenv("PASSWORD"))
        password_input.send_keys(Keys.ENTER)

    def handle_warehouse(self):
        """Enters the warehouse information on the FCLM Portal."""
        warehouse_input = self.driver.find_element(By.ID, "qlInput")
        warehouse_input.click()
        warehouse_input.send_keys("SMF9")
        warehouse_input.send_keys(Keys.ENTER)
