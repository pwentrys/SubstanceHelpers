from pathlib import Path

from templates.shelf import Shelf


class Shelves:
    # TODO obj for collection of shelf objs - helper for auto organizing
    # valid = ensure proper config.

    def __init__(self, shelves):
        """
        :param shelves: shelves = [Shelf objects]
        """
        self.shelves = []
        self.valid = False

        self.parse_shelves(shelves)

    def parse_shelves(self, shelves):
        if len(shelves) > 0:
            self.shelves = [Shelf(shelf) for shelf in shelves if Path.exists(shelf)]

        self.__validate__()

    def __validate__(self):
        self.valid = len(self.shelves) > 0
