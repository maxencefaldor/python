from q4 import encode


def test_simple():
    s = "AAABBBCCDAA"
    expected = "A3B3C2D1A2"
    output = encode(s)
    print(output)
    assert output == expected


def test_long_run():
    s = "AAAAAAAAAAAA"  # 12 A's
    expected = "A12"
    output = encode(s)
    print(output)
    assert output == expected


def test_no_runs():
    s = "abcdef"
    expected = "a1b1c1d1e1f1"
    output = encode(s)
    print(output)
    assert output == expected


def test_mixed():
    s = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    expected = "W12B1W12B3W24B1"
    output = encode(s)
    print(output)
    assert output == expected


def test_empty():
    s = ""
    expected = ""
    output = encode(s)
    print(output)
    assert output == expected


def test_single():
    s = "A"
    expected = "A1"
    output = encode(s)
    print(output)
    assert output == expected


if __name__ == "__main__":
    test_simple()
    test_long_run()
    test_no_runs()
    test_mixed()
    test_empty()
    test_single()
