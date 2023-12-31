from abc import ABC, abstractmethod


class Character(ABC):
    """Character abstract class"""
    def __init__(self, first_name, is_alive=True):
        """init a character"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """kill Character"""
        pass


class Stark(Character):
    """Stark class is a Character class representing the Stark family"""
    def __init__(self, first_name, is_alive=True):
        """init a Stark"""
        super().__init__(first_name, is_alive)

    def die(self):
        """kill a Stark"""
        self.is_alive = False
