class calculator:
    """
    Calculator class that can do calculation of 2 vectors.
    It Belongs to a class rather than an instance of the class.
    It does not operate on the instance's state and does not
    have access to instance-specific data or methods.

    Attributes :
    vectors (list) : The vectors to operate.

    Methods :
        dotproduct (list, list) : * each element of vectors between them.

        add_vec (list, list) : + each element of vectors between them.

        sous_vec (list, list) : - each element of vectors between them.
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Multiply each element of v1 and v2 between them.

        Args :
            V1, V2 (list[float], list[float]) : 2 list of float.
        """
        dot_product = 0.0
        for i in V1:
            dot_product += i * V2[V1.index(i)]
        print(f"Dot product is: {int(dot_product)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add each element of v1 and v2 between them.

        Args :
            V1, V2 (list[float], list[float]) : 2 list of float.
        """
        add_vec = []
        for i in V1:
            add_vec.append(float(i + V2[V1.index(i)]))
        print(f"Add Vector is : {add_vec}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Substract each element of v1 and v2 between them.

        Args :
            V1, V2 (list[float], list[float]) : 2 list of float.
        """
        sous_vec = []
        for i in V1:
            sous_vec.append(float(i - V2[V1.index(i)]))
        print(f"Sous Vector is: {sous_vec}")
