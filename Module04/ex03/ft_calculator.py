class calculator:
    """calculator class for vector and scalar calculations"""

    def __init__(self, vect) -> None:
        """Init a calculator object with a vector"""
        self._vect = vect

    def __add__(self, object) -> None:
        """Adds value of object to each value in vector"""
        self._vect = [x + object for x in self._vect]
        print(self._vect)

    def __mul__(self, object) -> None:
        """Multiplies value of object to each value in vector"""
        self._vect = [x * object for x in self._vect]
        print(self._vect)

    def __sub__(self, object) -> None:
        """Subtracts value of object from each value in vector"""
        self._vect = [x - object for x in self._vect]
        print(self._vect)

    def __truediv__(self, object) -> None:
        """Divides value of object by each value in vector"""
        if object == 0:
            return None
        self._vect = [x / object for x in self._vect]
        print(self._vect)
