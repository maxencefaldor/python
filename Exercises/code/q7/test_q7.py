from q7 import count_palindromes


def test_one_to_ten():
    count = count_palindromes(0, 10)
    print(count)
    assert count == 10


def test_one_to_hundred():
    count = count_palindromes(0, 100)
    print(count)
    assert count == 19


def test_three_digits():
    count = count_palindromes(100, 999)
    print(count)
    assert count == 90


def test_four_digits():
    count = count_palindromes(1000, 9999)
    print(count)
    assert count == 90


def test_arbitrary():
    count = count_palindromes(340, 450)
    print(count)
    assert count == 11


def test_same_start_and_end_is_palindrome():
    count = count_palindromes(2002, 2002)
    print(count)
    assert count == 1


def test_same_start_and_end_is_not_palindrome():
    count = count_palindromes(75, 75)
    print(count)
    assert count == 0
    
    
if __name__ == "__main__":
    test_one_to_ten()
    test_one_to_hundred()
    test_three_digits()
    test_four_digits()
    test_arbitrary()
    test_same_start_and_end_is_palindrome()
    test_same_start_and_end_is_not_palindrome()
    