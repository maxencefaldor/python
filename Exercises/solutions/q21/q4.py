def encode(s):
    if not s:
        return ""

    encoded = []
    i = 0
    n = len(s)

    while i < n:
        # This is the character for the current run
        char = s[i]
        count = 1

        # Move j forward as long as it's the same character
        j = i + 1
        while j < n and s[j] == char:
            count += 1
            j += 1

        # Append the run (e.g., "A12")
        encoded.append(f"{char}{count}")

        # Move i to the start of the next new character
        i = j

    return "".join(encoded)
