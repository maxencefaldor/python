import json
import os


def load_filesystem(json_filename):
    """Load the JSON file located next to this module (solutions/q8)."""
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, json_filename)
    with open(path, "r") as f:
        return json.load(f)


def find_files_by_extension(filesystem, extension):
    all_files = []

    # Start the recursive search.
    # We pass the root node's children and its path ("/")
    if "children" in filesystem:
        for child in filesystem["children"]:
            _find_recursive(child, "/", all_files, extension)

    return all_files


def _find_recursive(node, current_path, all_files, extension):
    """
    A helper function to recursively traverse the filesystem.

    Args:
        node: The current file/directory node (a dict).
        current_path: The path to this node's parent (e.g., "/home/user").
        all_files: The list to append results to.
        extension: The file extension to search for (e.g., ".txt").
    """
    node_name = node["name"]

    # Construct the full path for the current node
    # Handle the root's children (e.g., "/" + "home")
    if current_path == "/":
        new_path = f"/{node_name}"
    # Handle nested children (e.g., "/home" + "/" + "user")
    else:
        new_path = f"{current_path}/{node_name}"

    # Case 1: Node is a file
    if node["type"] == "file":
        if new_path.endswith(extension):
            all_files.append(new_path)

    # Case 2: Node is a directory
    elif node["type"] == "directory" and "children" in node:
        # Recurse for all children
        for child in node["children"]:
            _find_recursive(child, new_path, all_files, extension)
