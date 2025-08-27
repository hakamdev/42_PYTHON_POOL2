from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class to create a King"""

    def __init__(self, first_name):
        """init a King"""
        super().__init__(first_name)

    def set_eyes(self, eyes):
        """set eyes value"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        "set hairs value"
        self.hairs = hairs

    def get_eyes(self):
        "get eyes value"
        return self.eyes

    def get_hairs(self):
        "get hairs value"
        return self.hairs
