class calculator:

    def __init__(self, vect) -> None:
        self._vect = vect

    def __add__(self, object) -> None:
        res = map(lambda x: x + object, self._vect)
        print(list(res))

    def __mul__(self, object) -> None:
        print([x * object for x in self._vect])

    def __sub__(self, object) -> None:
        print([x - object for x in self._vect])

    def __truediv__(self, object) -> None:
        if object == 0:
            return None
        print([x / object for x in self._vect])
