from collections import defaultdict


def group_anagrams(words):
    anagram_groups = defaultdict(list)

    # Iterate through each word
    for word in words:
        # Create the canonical key by sorting the word's characters
        sorted_key = "".join(sorted(word))

        # Append the original word to the list for that key
        anagram_groups[sorted_key].append(word)

    # Convert to a regular dict and sort the value lists
    final_groups = {}
    for key, value in anagram_groups.items():
        final_groups[key] = sorted(value)

    return final_groups
