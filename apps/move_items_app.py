import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.interfaces import MoveAppInterface


class MoveItemsApp(MoveAppInterface):
    def __init__(self):
        self.driver = None
        self.wait = None

    def goto_app(self, driver, wait):
        """Redirect to the MoveItems App."""
        self.driver = driver
        self.wait = wait
        self.driver.get(os.getenv("MOVE_LINK"))
        self.wait.until(EC.visibility_of_element_located((By.ID, "a-page")))
        self.switch_mode()

    def switch_mode(self):
        """Check and change the MoveItems app to container mode."""
        text = self.driver.find_element(By.ID, "context").text
        if text != "Mode:\nContainer":
            self.driver.find_element(By.XPATH, "//a[contains(text(), 'User menu')]").click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Change mode']")))
            self.driver.find_element(By.XPATH, "//h1[text()='Change mode']").click()

            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Select mode']")))
            self.driver.find_element(By.XPATH, "//input[@value='CONTAINER']/..").click()
            self.driver.find_element(By.ID, "a-autoid-0").click()

            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Scan container']")))

    def move_tote(self, tote1, tote2):
        """Move tote from one container to another designated container."""
        self.driver.find_element(By.TAG_NAME, "input").send_keys(tote1)
        self.driver.find_element(By.CLASS_NAME, "a-button-input").click()

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Confirm move']")))
        self.driver.find_element(By.CLASS_NAME, "a-button-input").click()

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Scan destination container']")))

        self.driver.find_element(By.TAG_NAME, "input").send_keys(tote2)
        self.driver.find_element(By.CLASS_NAME, "a-button-input").click()

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Success']")))
        self.driver.find_element(By.CLASS_NAME, "a-button-inner").click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Scan container']")))
