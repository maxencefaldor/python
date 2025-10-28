from q1 import count_vowels


def test_zero():
    count = count_vowels("lymph")
    print(count)
    assert count == 0

def test_one():
    count = count_vowels("python")
    print(count)
    assert count == 1

def test_two():
    count = count_vowels("snake")
    print(count)
    assert count == 2

def test_three():
    count = count_vowels("neutral")
    print(count)
    assert count == 3
    
def test_four():
    count = count_vowels("binary number")
    print(count)
    assert count == 4
    
def test_five():
    count = count_vowels("very good exam")
    print(count)
    assert count == 5


if __name__ == "__main__":
    test_zero()
    test_one()
    test_two()
    test_three()
    test_four()
    test_five()
    