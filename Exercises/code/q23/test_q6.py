from q6 import get_error_summary


def test_log_summary():
    output = get_error_summary("access.log")
    print(output)

    expected = {
        "Failed to connect to database": 3,
        "User login failed: user_xyz": 2,
        "Disk space low": 1,
        "Null pointer exception at com.example.Module:42": 1,
    }

    assert output == expected


def test_empty_log():
    output = get_error_summary("empty.log")
    print(output)
    assert output == {}


def test_no_errors_log():
    output = get_error_summary("no_errors.log")
    print(output)
    assert output == {}


if __name__ == "__main__":
    test_log_summary()
    test_empty_log()
    test_no_errors_log()
