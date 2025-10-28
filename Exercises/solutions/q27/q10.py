import json
import csv
import os


class FileProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.data = None  # To store loaded data

    def read(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def process(self):
        raise NotImplementedError("Subclass must implement abstract method")


class CsvProcessor(FileProcessor):
    def read(self):
        # Only read if data hasn't been loaded yet
        if self.data is None:
            self.data = []
            base_dir = os.path.dirname(__file__)
            path = os.path.join(base_dir, self.filename)
            with open(path, "r", newline="") as f:
                # Use the csv module to handle commas, quotes, etc.
                reader = csv.reader(f)
                self.data = list(reader)

    def process(self):
        # Ensure data is loaded
        self.read()

        if not self.data:
            return []

        header = self.data[0]
        processed_data = []

        # Convert list-of-lists to list-of-dicts
        for row in self.data[1:]:
            # Use a dictionary comprehension to map headers to row values
            row_dict = {header[i]: row[i] for i in range(len(header))}
            processed_data.append(row_dict)

        return processed_data


class JsonProcessor(FileProcessor):
    def read(self):
        # Only read if data hasn't been loaded yet
        if self.data is None:
            base_dir = os.path.dirname(__file__)
            path = os.path.join(base_dir, self.filename)
            with open(path, "r") as f:
                self.data = json.load(f)

    def process(self):
        # Ensure data is loaded
        self.read()

        # JSON is already in the correct dict format, so just return
        return self.data


def process_files(processors):
    """
    Takes a list of FileProcessor objects and returns
    a list of their processed data.
    """
    results = []
    # This loop demonstrates polymorphism:
    # Python calls the correct .process() method (Csv or Json)
    # based on the object's actual type.
    for processor in processors:
        results.append(processor.process())
    return results
