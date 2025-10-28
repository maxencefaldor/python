import sys
from io import StringIO

from monster import Monster
from q9 import Python

def test_move():
    python = Python()
    output = python.move()
    assert output == "sliding"


def test_roar():
    python = Python()
    output = python.roar()
    assert output == "hiss"


def test_is_monster():
    python = Python()
    assert isinstance(python, Monster)


def test_attack():
    # To store your printed output in a buffer
    # so that I can compare what you printed with the expected output
    old_stdout = sys.stdout
    output = StringIO()
    sys.stdout = output

    python = Python()
    python.attack()

    # Now actually printing out your output from the buffer
    sys.stdout = old_stdout
    print(output.getvalue(), end="")

    expected_output = """Initialising Monster.
sliding
hiss
kicking
hiss
sleeping"""

    assert expected_output.strip() == output.getvalue().strip() 


if __name__ == "__main__":
    test_move()
    test_roar()
    test_is_monster()
    test_attack()

