from q3 import roman_to_int


def test_simple():
    assert roman_to_int("I") == 1
    assert roman_to_int("II") == 2
    assert roman_to_int("III") == 3


def test_subtraction():
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("XL") == 40
    assert roman_to_int("XC") == 90
    assert roman_to_int("CD") == 400
    assert roman_to_int("CM") == 900


def test_complex_1():
    s = "LVIII"
    # L = 50, V = 5, III = 3
    expected = 58
    output = roman_to_int(s)
    print(f"{s} -> {output}")
    assert output == expected


def test_complex_2():
    s = "MCMXCIV"
    # M = 1000, CM = 900, XC = 90, IV = 4
    expected = 1994
    output = roman_to_int(s)
    print(f"{s} -> {output}")
    assert output == expected


def test_complex_3():
    s = "CDXLIV"
    # CD = 400, XL = 40, IV = 4
    expected = 444
    output = roman_to_int(s)
    print(f"{s} -> {output}")
    assert output == expected


if __name__ == "__main__":
    test_simple()
    test_subtraction()
    test_complex_1()
    test_complex_2()
    test_complex_3()
