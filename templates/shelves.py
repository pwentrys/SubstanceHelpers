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
        """
        Parse string shelf objs to shelves objs.
        :param shelves: 
        :return: 
        """
        if len(shelves) > 0:
            self.shelves = [Shelf(shelf) for shelf in shelves]

        self.__validate__()

    def __validate__(self):
        """
        essentially .isValid() check.
        :return: 
        """
        self.valid = len(self.shelves) > 0
