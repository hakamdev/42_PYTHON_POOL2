class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = sum([V1[i] * V2[i] for i in range(len(V1))])
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = map(float, [V1[i] + V2[i] for i in range(len(V1))])
        print(f"Add Vector is : {list(result)}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = map(float, [V1[i] - V2[i] for i in range(len(V1))])
        print(f"Sous Vector is: {list(result)}")
