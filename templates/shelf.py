from pathlib import Path


class Shelf:
    # path = io path
    # valid = ensure proper config.

    def __init__(self, path):
        self.path = Path(path)
        self.valid = False

        self.__validate__()

    def __validate__(self):
        """
        essentially .isValid() check.
        :return: 
        """
        self.valid = self.path.exists()
