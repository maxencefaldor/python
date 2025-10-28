from q8 import load_filesystem, find_files_by_extension


def test_find_txt():
    fs = load_filesystem("filesystem.json")
    files = find_files_by_extension(fs, ".txt")
    print(files)
    # The order doesn't matter, so we test with sets
    assert set(files) == {"/home/user/profile.txt", "/home/user/docs/notes.txt"}


def test_find_pdf():
    fs = load_filesystem("filesystem.json")
    files = find_files_by_extension(fs, ".pdf")
    print(files)
    assert set(files) == {"/home/user/docs/report.pdf"}


def test_find_md():
    fs = load_filesystem("filesystem.json")
    files = find_files_by_extension(fs, ".md")
    print(files)
    assert set(files) == {"/README.md"}


def test_find_log():
    fs = load_filesystem("filesystem.json")
    files = find_files_by_extension(fs, ".log")
    print(files)
    assert set(files) == {"/system.log"}


def test_not_found():
    fs = load_filesystem("filesystem.json")
    files = find_files_by_extension(fs, ".zip")
    print(files)
    assert set(files) == set()


def test_empty():
    fs = load_filesystem("empty_fs.json")
    files = find_files_by_extension(fs, ".txt")
    print(files)
    assert set(files) == set()


if __name__ == "__main__":
    test_find_txt()
    test_find_pdf()
    test_find_md()
    test_find_log()
    test_not_found()
    test_empty()
