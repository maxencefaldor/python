from q10 import CsvProcessor, JsonProcessor, process_files, FileProcessor


def test_file_processors():
    # Expected data
    expected_data = [
        {"id": "1", "name": "Alice", "role": "Engineer"},
        {"id": "2", "name": "Bob", "role": "Manager"},
        {"id": "3", "name": "Charlie", "role": "Designer"},
    ]

    # Create processor instances
    csv_proc = CsvProcessor("data.csv")
    json_proc = JsonProcessor("data.json")

    # Test polymorphism in process_files
    # process_files should call .process() on each object
    all_data = process_files([csv_proc, json_proc])

    print("CSV Data:", all_data[0])
    print("JSON Data:", all_data[1])

    assert all_data[0] == expected_data
    assert all_data[1] == expected_data

    # Test base class raises error
    try:
        base_proc = FileProcessor("data.csv")
        base_proc.process()
        assert False, "FileProcessor.process() did not raise NotImplementedError"
    except NotImplementedError:
        pass  # Correct!


if __name__ == "__main__":
    test_file_processors()
