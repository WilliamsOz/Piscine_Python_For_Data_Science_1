from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class representing a character.
    """

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Constructor for Character class.

        Args :
            first_name (str) : A string representing the name of the character.
            is_alive (bool) : A state of the character, true by default.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Method to change the state of an character.

        It should be implemented in subclasses to change the state of
        a character from alive to dead.
        """
        pass

class Stark(Character):
    """
    Class representing a "Stark" character, inherit from Character class.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Constructor for Stark class.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        This method override the abstract method and change the state
        of is_alive to False.
        """
        self.is_alive = False
