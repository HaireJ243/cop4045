from numbers import Real
from testif import testif

class NVector:
    """Represent a vector of real numbers in a python list"""

    def __init__(self, *args: object) -> None:
        """Create a vector from one sequence or two or more numbers.

            The vector makes a new list, so original list does not change
            vector."""

        if len(args) == 0:

            raise TypeError("NVector needs an argument")

        if len(args) == 1:

            self.elements: list[Real] = list(args[0])
        else:
            self.elements = list(args)

        for value in self.elements:
            if not isinstance(value, Real):
                raise TypeError("Vector elements must be real numbers")

    def __len__(self) -> int:
        """Return number of elements in vector"""

        return len(self.elements)

    def __getitem__(self, index: int) -> Real:
        """Return element at index"""

        return self.elements[index]

    def __setitem__(self, index: int, value: Real) -> None:
        """Replace element at index with value"""

        if not isinstance(value, Real):
            raise TypeError("Vector elements must be real numbers")
        self.elements[index] = value

    def __str__(self) -> str:
        """Return readable string with vector's elements"""

        return str(self.elements)

    def __eq__(self, other: object) -> bool:
        """Return True when other IS an equal NVector"""

        return isinstance(other, NVector) and self.elements == other.elements

    def __ne__(self, other: object) -> bool:
        """Return True when other is NOT an equal NVector"""

        return not self == other

    def __add__(self, other: object) -> "NVector":
        """Return a new vector after adding vector or number"""

        if isinstance(other, NVector):

            if len(self) != len(other):
                raise ValueError("Vectors must be equal length")

            answer = []

            for i in range(len(self)):
                answer.append(self[i] + other[i])
            return NVector(answer)

        if isinstance(other, Real):

            answer = []
            for value in self.elements:
                answer.append(value + other)

            return NVector(answer)

        raise TypeError("Can only add number or NVector")

    def __radd__(self, other: object) -> "NVector":
        """Return result of number plus vector"""

        return self + other

    def __mul__(self, other: object) -> "NVector | Real":
        """Return scalar multiplication or dot product of two vectors"""

        if isinstance(other, NVector):

            if len(self) != len(other):
                raise ValueError("Vectors must be equal length")

            total : Real = 0
            for i in range(len(self)):

                total += self[i] * other[i]
            return total

        if isinstance(other, Real):

            answer = []

            for value in self.elements:
                answer.append(value * other)

            return NVector(answer)

        raise TypeError("can only multiply by a number or NVector")

    def __rmul__(self, other: object) -> "NVector | Real":
        """Return result of number * vector"""

        return self * other

    @classmethod
    def zeros(cls, n: int) -> "NVector":
        """Return new vector containing zeros"""

        if n < 0:

            raise ValueError("Length cannot be negative")

        return cls([0] * n)

def main() -> None:
    """Test NVector methods"""

    v = NVector(3, 0, 1, -1)
    w = NVector([1, 2, 3, 4])

    testif(len(v) == 4, "len", "works", "failed")
    testif(v[1] == 0 and v[-2] == 1, "getitem", "works", "failed")

    v[2] = 5

    testif(v[2] == 5, "setitem", "works", "failed")
    testif(v == NVector(3, 0, 5, -1), "equality, works", "failed")

    testif(NVector(3, 0, 1, -1) + w == NVector(4, 2, 4, 3), "vector addition",
           "works", "failed")

    testif(NVector(3, 0, 1, -1) + 10 == NVector(13, 10, 11, 9), "scalar addition",
           "works", "failed")

    testif(10 + NVector(3, 0, 1, -1) == NVector(13, 10, 11, 9),
               "reflected addition", "works", "failed")
    
    testif(NVector(3, 0, 1, -1) * w == 2,
               "dot product", "works", "failed")
    
    testif(2 * NVector(3, 0, 1, -1) == NVector(6, 0, 2, -2),
               "scalar multiplication", "works", "failed")
    
    testif(NVector.zeros(3) == NVector(0, 0, 0), "zeros", "works", "failed")

if __name__ == "__main__":
    main()