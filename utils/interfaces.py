from abc import ABC, abstractmethod


class BusinessLogicInterface(ABC):
    @abstractmethod
    def move_totes(self):
        pass


class FileHandlerInterface(ABC):
    @abstractmethod
    def read_totes(self):
        pass


class DriverInterface(ABC):
    @abstractmethod
    def setup_driver(self):
        pass


class LoginHandlerInterface(ABC):
    @abstractmethod
    def sign_in(self, driver):
        pass


class MoveAppInterface(ABC):
    @abstractmethod
    def goto_app(self, driver, wait):
        pass

    def move_tote(self, tote1, tote2):
        pass
