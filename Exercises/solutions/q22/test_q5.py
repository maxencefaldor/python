from q5 import decode


def test_simple():
    s = "A3B3C2D1A2"
    expected = "AAABBBCCDAA"
    output = decode(s)
    print(output)
    assert output == expected


def test_long_run():
    s = "A12"
    expected = "AAAAAAAAAAAA"
    output = decode(s)
    print(output)
    assert output == expected


def test_no_runs():
    s = "a1b1c1d1e1f1"
    expected = "abcdef"
    output = decode(s)
    print(output)
    assert output == expected


def test_mixed():
    s = "W12B1W12B3W24B1"
    expected = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    output = decode(s)
    print(output)
    assert output == expected


def test_empty():
    s = ""
    expected = ""
    output = decode(s)
    print(output)
    assert output == expected


def test_single():
    s = "A1"
    expected = "A"
    output = decode(s)
    print(output)
    assert output == expected


if __name__ == "__main__":
    test_simple()
    test_long_run()
    test_no_runs()
    test_mixed()
    test_empty()
    test_single()
