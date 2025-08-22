import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def goto_app(driver, wait):
    """Redirect to the MoveItems App."""
    driver.get(os.getenv("MOVE_LINK"))
    wait.until(EC.visibility_of_element_located((By.ID, "a-page")))
    _switch_mode(driver, wait)


def _switch_mode(driver, wait):
    """Check and change the MoveItems app to container mode."""
    wait.until(EC.visibility_of_element_located((By.ID, "context")))
    text = driver.find_element(By.ID, "context").text
    if text != "Mode:\nContainer":
        driver.find_element(By.XPATH, "//a[contains(text(), 'User menu')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Change mode']")))
        driver.find_element(By.XPATH, "//h1[text()='Change mode']").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Select mode']")))
        driver.find_element(By.XPATH, "//input[@value='CONTAINER']/..").click()
        driver.find_element(By.ID, "a-autoid-0").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Scan container']")))


def move_tote(driver, wait, tote1, tote2):
    """Move tote from one container to another designated container."""
    driver.find_element(By.TAG_NAME, "input").send_keys(tote1)
    driver.find_element(By.CLASS_NAME, "a-button-input").click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Confirm move']")))
    driver.find_element(By.CLASS_NAME, "a-button-input").click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Scan destination container']")))

    driver.find_element(By.TAG_NAME, "input").send_keys(tote2)
    driver.find_element(By.CLASS_NAME, "a-button-input").click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Success']")))
    driver.find_element(By.CLASS_NAME, "a-button-inner").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Scan container']")))
