from utils.interfaces import FileHandlerInterface


class FileHandler(FileHandlerInterface):
    def read_totes(self):
        """Reads and returns the totes listed in the file."""
        with open("../txt/totes.txt", "r") as file:
            totes = file.readlines()
        return totes
