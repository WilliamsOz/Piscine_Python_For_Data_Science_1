class calculator:
    """
    Calculator class that can do additions, multiplication, sub- traction,
    division of vector with scalar.

    Attributes :
        vector (list) : The vector on which operations will be performed.

    Methods :
        __init__ (self, vector) : Init the calculator with the provided vector.

        __add__ (self, obj) : + each element of vector with obj.

        __mul__ (self, obj) : * each element of vector with obj.

        __sub__ (self, obj) : - each element of vector with obj.

        __truediv__ (self, obj) : / each element of vector with obj.
    """
    def __init__(self, vector) -> None:
        """
        Initialize the vector vector given.

        Args :
            vector (list) : A vector to operate on.
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """
        Adding object to each element of vector.

        Args :
            object : An object to add to each element of the vector.

        Returns :
            The vector after the operation.
        """
        self.vector = [item + object for item in self.vector]
        print(self.vector)
        return self.vector

    def __mul__(self, object) -> None:
        """
        Multiplicate object to each element of vector.

        Args :
            object : An object to add to each element of the vector.

        Returns :
            The vector after the operation.
        """
        self.vector = [item * object for item in self.vector]
        print(self.vector)
        return self.vector

    def __sub__(self, object) -> None:
        """
        Adding object to each element of vector.

        Args :
            object : An object to add to each element of the vector.

        Returns :
            The vector after the operation.
        """
        self.vector = [item - object for item in self.vector]
        print(self.vector)
        return self.vector

    def __truediv__(self, object) -> None:
        """
        Adding object to each element of vector.

        Args :
            object : An object to add to each element of the vector.

        Returns :
            The vector after the operation.
        """
        try:
            if object == 0:
                raise ZeroDivisionError("Can't divide by zero.")
            self.vector = [item / object for item in self.vector]
            print(self.vector)
            return self.vector
        except ZeroDivisionError as error:
            print("\033[31m", ZeroDivisionError.__name__ + ":",
                  error, "\033[0m")
