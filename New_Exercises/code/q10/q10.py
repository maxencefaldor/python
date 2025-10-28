class FileProcessor:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def process(self):
        raise NotImplementedError("Subclass must implement abstract method")


class CsvProcessor(FileProcessor):
    def read(self):
        pass  # TODO

    def process(self):
        pass  # TODO


class JsonProcessor(FileProcessor):
    def read(self):
        pass  # TODO

    def process(self):
        pass  # TODO


def process_files(processors):
    """
    Takes a list of FileProcessor objects and returns
    a list of their processed data.
    """
    results = []
    for processor in processors:
        results.append(processor.process())
    return results
