from S1E9 import Character


class Baratheon(Character):
    """Class to create a Baratheon character"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return "Vector: ('Baratheon', 'brown', 'dark')"

    def die(self):
        """kill a Baratheon"""
        self.is_alive = False

    # override __str__ method so it outputs: 
    # <bound method Baratheon.__str__ of Vector: ('Baratheon', 'brown', 'dark')>
    def __str__(self):
        return ("Bratheon", "brown", "dark")


class Lannister(Character):
    """Class to create a Lannister character"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return "Vector: ('Lannister', 'blue', 'light')"

    def die(self):
        """kill a Lannister"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """create a Lannister"""
        return cls(first_name, is_alive)
