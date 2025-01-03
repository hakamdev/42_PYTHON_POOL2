from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name):
        super().__init__(first_name)
        # self.family_name = "Lannister"
        # self.eyes = "blue"
        # self.hairs = "light"

    def set_eyes(self, eyes):
        self.eyes = eyes

    def set_hairs(self, hairs):
        self.hairs = hairs

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs
