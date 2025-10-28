from collections import defaultdict


def invert_dictionary(d):
    inverted_dict = defaultdict(list)

    # Populate the dictionary with keys as values and values as keys
    for key, value in d.items():
        inverted_dict[value].append(key)

    # Convert back to a regular dict and sort the lists
    final_dict = {}
    for key, value in inverted_dict.items():
        final_dict[key] = sorted(value)

    return final_dict
