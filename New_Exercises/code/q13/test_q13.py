from q13 import can_segment


def test_simple_true():
    s = "imperial"
    word_set = {"imperial", "college"}
    assert can_segment(s, word_set) == True


def test_two_words_true():
    s = "imperialcollege"
    word_set = {"imperial", "college"}
    assert can_segment(s, word_set) == True


def test_simple_false():
    s = "imperialcollegex"
    word_set = {"imperial", "college"}
    assert can_segment(s, word_set) == False


def test_example_1():
    s = "catsanddog"
    word_set = {"cats", "dog", "sand", "and", "cat"}
    # Can be "cats", "and", "dog"
    assert can_segment(s, word_set) == True


def test_example_2():
    s = "catsandog"
    word_set = {"cats", "dog", "sand", "and", "cat"}
    assert can_segment(s, word_set) == False


def test_reuse():
    s = "aaaaaaa"
    word_set = {"a", "aa", "aaa"}
    # e.g., "aaa", "aaa", "a"
    assert can_segment(s, word_set) == True


def test_long_fail():
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    word_set = {"a", "aa", "aaa", "aaaa", "aaaaa"}
    # This test checks for efficiency. A bad recursive solution
    # might time out.
    print("Running long efficiency test...")
    assert can_segment(s, word_set) == False
    print("Long test passed.")


if __name__ == "__main__":
    test_simple_true()
    test_two_words_true()
    test_simple_false()
    test_example_1()
    test_example_2()
    test_reuse()
    test_long_fail()
