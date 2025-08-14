import utils
from webdrivers.chrome_driver import ChromeDriver
from apps.move_items_app import MoveItemsApp


def main():
    file_handler = utils.FileHandler()
    driver_obj = ChromeDriver()
    driver, wait = driver_obj.setup_driver()
    login_handler = utils.FCLMSignIn()
    app = MoveItemsApp()

    business_logic = utils.MoveBack(
        file_handler,
        driver,
        wait,
        login_handler,
        app
    )
    business_logic.move_totes()

    driver.quit()


if __name__ == "__main__":
    main()
