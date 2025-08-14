from selenium.webdriver.support.wait import WebDriverWait
from interfaces import (BusinessLogicInterface,
                        FileHandlerInterface,
                        DriverInterface,
                        LoginHandlerInterface,
                        MoveAppInterface)


class MoveBack(BusinessLogicInterface):
    def __init__(self,
                 file_handler: FileHandlerInterface,
                 driver: DriverInterface,
                 wait: WebDriverWait,
                 login_handler: LoginHandlerInterface,
                 app: MoveAppInterface):
        self.file_handler = file_handler
        self.driver = driver
        self.wait = wait
        self.login_handler = login_handler
        self.app = app

    def move_totes(self):
        totes = self.get_totes()
        self.login_handler.sign_in(self.driver)
        self.app.goto_app(self.driver, self.wait)

        for tote in totes:
            self.move_container(tote)

    def get_totes(self):
        """Gets a list of strings representing totes that need to be moves."""
        totes = self.file_handler.read_totes()
        return totes

    def move_container(self, tote):
        """Moves a container to a dummy tote and moves it back to its original location."""
        self.app.move_tote(tote.strip(), "tsXX")
        self.app.move_tote("tsXX", tote.strip())
