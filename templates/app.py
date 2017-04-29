from pathlib import Path

from templates.shelves import Shelves


# TODO improve doc
class App:
    # Application base
    def __init__(self, name, path, shelves):
        """
        :param name: = human readable app name - ex -"Painter"
        :param path: = base dir which contains executable - ex: "C:/Program Files/Allegorithmic/Substance Painter 2"
        :param shelves: = [shelf location strings]
        """
        self.name = name
        self.path = path
        self.shelves = Shelves(shelves)
        self.valid = True

        self.__validate__()

    # Validate object
    def __validate__(self):
        # Ensure we have shelves
        if not self.shelves.valid:
            self.valid = False
            f"{self.name} - No Shelves"
            return

        # Ensure path exists
        if not Path.exists(self.path):
            self.valid = False
            f"{self.name} - Invalid Path: {self.path}"
            return

        self.valid = True
