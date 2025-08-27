class calculator:
    """calculator class for vector and vector calculations"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculates dot product of two vectors"""
        result = sum([V1[i] * V2[i] for i in range(len(V1))])
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Adds each value of first vector to each value of second vector"""
        result = map(float, [V1[i] + V2[i] for i in range(len(V1))])
        print(f"Add Vector is : {list(result)}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtracts each value of first\
 vector from each value of second vector"""
        result = map(float, [V1[i] - V2[i] for i in range(len(V1))])
        print(f"Sous Vector is: {list(result)}")
