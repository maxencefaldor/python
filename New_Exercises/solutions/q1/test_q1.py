from q1 import invert_dictionary


def test_simple():
    d = {"a": 1, "b": 2, "c": 1}
    expected = {1: ["a", "c"], 2: ["b"]}
    output = invert_dictionary(d)
    print(output)
    assert output == expected


def test_strings():
    d = {"apple": "fruit", "banana": "fruit", "carrot": "vegetable"}
    expected = {"fruit": ["apple", "banana"], "vegetable": ["carrot"]}
    output = invert_dictionary(d)
    print(output)
    assert output == expected


def test_mixed():
    d = {1: "a", "b": 2, 3: "a", "d": 2}
    expected = {"a": [1, 3], 2: ["b", "d"]}
    output = invert_dictionary(d)
    print(output)
    assert output == expected


def test_empty():
    d = {}
    expected = {}
    output = invert_dictionary(d)
    print(output)
    assert output == expected


def test_single():
    d = {"key1": "val1"}
    expected = {"val1": ["key1"]}
    output = invert_dictionary(d)
    print(output)
    assert output == expected


if __name__ == "__main__":
    test_simple()
    test_strings()
    test_mixed()
    test_empty()
    test_single()
