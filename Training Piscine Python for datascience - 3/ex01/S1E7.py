from S1E9 import Character


class Baratheon(Character):
    """
    Class representing a "Baratheon" character,
    inherit from Character class.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Baratheon character with the name given.

        Args :
            first_name (str) : A string representing the name of the character.
            is_alive (bool) : A state of the character, true by default.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        Method to change the state of an character to False.
        """
        self.is_alive = False

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"{self.__str__()}"


class Lannister(Character):
    """
    Class representing a "Lannister" character,
    imherit from Character class.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Lannister character with the name given.

        Args :
            first_name (str) : A string representing the name of the character.
            is_alive (bool) : A state of the character, true by default.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """
        Method to change the state of an character to False.
        """
        self.is_alive = False

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"{self.__str__()}"

    @classmethod
    def create_lannister(cls, fisrt_name, is_alive):
        """
        Create a Lannister character custom state of is_alive.

        Args :
            first_name (str) : A string representing the name of the character.
            is_alive (bool) : A state of the character, true by default.
            cls refer to the class itself and not to the instance compare to
            self.
        """
        instance = cls(fisrt_name)
        instance.is_alive = is_alive
        return instance
