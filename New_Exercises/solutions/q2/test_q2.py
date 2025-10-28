from q2 import group_anagrams


def test_example_1():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = group_anagrams(words)
    expected = {"aet": ["ate", "eat", "tea"], "ant": ["nat", "tan"], "abt": ["bat"]}
    print(output)
    assert output == expected


def test_example_2():
    words = ["listen", "silent", "enlist", "google"]
    output = group_anagrams(words)
    expected = {"eilnst": ["enlist", "listen", "silent"], "eggloo": ["google"]}
    print(output)
    assert output == expected


def test_single():
    words = ["a"]
    output = group_anagrams(words)
    expected = {"a": ["a"]}
    print(output)
    assert output == expected


def test_empty():
    words = []
    output = group_anagrams(words)
    expected = {}
    print(output)
    assert output == expected


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_single()
    test_empty()
