import json


def load_filesystem(json_filename):
    """A helper function to load the JSON file."""
    with open(json_filename, "r") as f:
        return json.load(f)


def find_files_by_extension(filesystem, extension):
    # Hint: You will likely want to create a helper function
    # that takes the current node and the current path as arguments.
    pass
