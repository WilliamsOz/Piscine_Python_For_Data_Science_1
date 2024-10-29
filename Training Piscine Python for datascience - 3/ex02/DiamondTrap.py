from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Create a monster called Joffrey Baratheon.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a King character with the name given.

        Args :
            first_name (str) : A string representing the name of the character.
            is_alive (bool) : A state of the character, true by default.
        """
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """
        Get the eyes's color of the character.
        """
        return self.eyes

    def set_eyes(self, color):
        """
        Set the eyes's color of the character.
        """
        self.eyes = color

    def get_hairs(self):
        """
        Get the hair's color of the character.
        """
        return self.hairs

    def set_hairs(self, color):
        """
        Set the hair's color of the character.
        """
        self.hairs = color
