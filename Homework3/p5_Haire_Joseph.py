import turtle
from testif import testif

def draw_leaf_branch(length: float, level: int, curved: bool) -> None:
    """Draw a branch recursively"""

    if level == 0:
        return

    if curved:
        turtle.circle(length * 4, 14)
    else:
        turtle.forward(length)

    position = turtle.position()
    heading  = turtle.heading()

    turtle.left(35)
    draw_leaf_branch(length * 0.72, level -1, curved)

    turtle.up()
    turtle.goto(position)
    turtle.setheading(heading)
    turtle.down()
    turtle.right(35)
    draw_leaf_branch(length * 0.72, level -1, curved)

    turtle.up()
    turtle.goto(position)
    turtle.setheading(heading)
    turtle.down()

def draw_leaf_straight(
        recursion_level: int,
        petiole_length: float,
        x_position: float = 0.0
    ) -> None:
    """Draw a vertical, recursively branching leaf"""

    if recursion_level < 1:
        raise ValueError("recursion_level must be at least 1")
    if petiole_length <= 0:
        raise ValueError("petiole_length must be positive")

    turtle.delay(0)
    turtle.speed(0)
    turtle.up()
    turtle.goto(x_position, -petiole_length)
    turtle.setheading(0)
    turtle.left(90)
    turtle.down()
    turtle.forward(petiole_length)
    draw_leaf_branch(petiole_length * 0.65, recursion_level + 1, False)

def draw_leaf_curved(
        recursion_level: int,
        petiole_length: float,
        x_position: float = 0.0
    ) -> None:
    """Draw a vertical leafe with curved branches"""

    if recursion_level < 1:
        raise ValueError("recursion_level must be at least 1")
    if petiole_length <= 0:
        raise ValueError("petiole_length must be positive")

    turtle.delay(0)
    turtle.speed(0)
    turtle.up()
    turtle.goto(x_position, -petiole_length)
    turtle.setheading(0)
    turtle.left(90)
    turtle.down()
    turtle.forward(petiole_length)
    draw_leaf_branch(petiole_length * 0.65, recursion_level + 1, True)

def display_leaf_examples() -> None:
    """Display recursive leaves."""

    screen = turtle.Screen()
    screen.setup(width=1200, height=700)
    screen.setworldcoordinates(-600, -260, 600, 300)
    screen.title("Recursive Leaf Examples")
    screen.bgcolor("white")
    screen.tracer(0, 0)
    turtle.hideturtle()
    turtle.pensize(0.7)

    examples = (
        (-380, draw_leaf_straight, 8, "Straight leaf (level 8)"),
        (0, draw_leaf_straight, 1, "Straight leaf (level 1)"),
        (380, draw_leaf_curved, 8, "Curved leaf (level 8)"),
    )

    for x_position, draw_leaf, recursion_level, label in examples:
        draw_leaf(recursion_level, 120, x_position)
        turtle.penup()
        turtle.goto(x_position, -225)
        turtle.write(label, align="center", font=("Arial", 11, "normal"))

    screen.update()
    turtle.done()

def strB(n:int, base:int = 10) -> str:
    """Recursively conver non-negative int to a string"""

    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be non-negative int")
    if not isinstance(base, int) or not 2 <= base <= 26:
        raise ValueError("base must be an int between 2 and 26")

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < base:
        return digits[n]
    return strB(n // base, base) + digits[n % base]

def test_strB() -> None:
    """Test strB with decimal, binary, and alphabetic digits."""

    testif(strB(0) == "0", "strB zero")
    testif(strB(73, 8) == "111", "strB octal")
    testif(strB(987, 16) == "3DB", "strB hexadecimal")
    testif(strB(12345, 26) == "I6L", "strB base 26")

def cnk_recursive(n: int, k: int, memo: dict[tuple[int,int], int]) -> int:
    """Return n choose k using the recurrence and shared memo dict"""

    if k == 0 or k == n:
        return 1

    key = (n,k)

    if key not in memo:
        memo[key] = (cnk_recursive(n - 1, k - 1, memo) + 
                     cnk_recursive(n - 1, k, memo))
    return memo[key]

def Cnk_m(n: int, k: int) -> int:
    """Compute coefficient recursively with memoization"""

    if not isinstance(n, int) or not isinstance(k, int):
        raise ValueError("n and k must be ints")
    if n < 0 or k < 0 or k > n:
        raise ValueError("requires n >= 0 and 0 <= k <= n")

    return cnk_recursive(n, min(k, n-k), {})

def test_Cnk_m() -> None:
    """test memoized binomial coefficients"""

    testif(Cnk_m(5, 2) == 10, "Cnk_m 5 choose 2")
    testif(Cnk_m(10, 0) == 1, "Cnk_m 10 choose 0")
    testif(Cnk_m(20, 10) == 184756, "Cnk_m 20 choose 10")
    testif(Cnk_m(30, 3) == 4060, "Cnk_m 30 choose 3")

def run_Cnk() -> None:
    """Print several binomial coefficients for console demonstrations"""

    for n, k in ((20, 10), (30, 15), (50, 25)):
        print(f"C({n}, {k}) = {Cnk_m(n,k)}")

def make_pairs(
        seq1: list[object],
        seq2: list[object],
        accumulator: list[tuple[object, object]] | None = None
    ) -> list[tuple[object,object]]:
    """Recursively pair elements up to the shorter list"""

    if accumulator is None:
        accumulator = []
    if not seq1 or not seq2:
        return accumulator

    accumulator.append((seq1[0], seq2[0]))
    return make_pairs(seq1[1:], seq2[1:], accumulator)

def test_make_pairs() -> None:
    """Test make_pairs, including inputs that stop at an empty list."""

    testif(make_pairs([1, 2, 3], [4, 5, 6]) ==
           [(1, 4), (2, 5), (3, 6)], "make_pairs equal lengths")
    
    testif(make_pairs([1, 2, 3], [4, 5]) ==
           [(1, 4), (2, 5)], "make_pairs second list shorter")
    
    testif(make_pairs([1, 2], [4, 5, 6]) ==
           [(1, 4), (2, 5)], "make_pairs first list shorter")
    
    testif(make_pairs([], [4, 5]) == [], "make_pairs empty first list")
    testif(make_pairs([1, 2], []) == [], "make_pairs empty second list")

def run_strB() -> None:
    """Print conversions using values different from assignment examples"""

    for n, base in ((42, 2), (314, 12), (2026, 26)):
        print(f"strB({n}, base = {base}) = {strB(n, base)}")

def main() -> None:
    """Run functions and tests"""

    test_strB()
    test_Cnk_m()
    test_make_pairs()
    run_strB()
    run_Cnk()
    display_leaf_examples()

if __name__ == "__main__":
    main()
