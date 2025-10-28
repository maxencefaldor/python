def decode(s):
    decoded = []
    i = 0
    n = len(s)

    while i < n:
        # The character is at position i
        char = s[i]
        i += 1

        # The number starts at i
        num_str = ""
        # Keep reading digits until we hit a non-digit or end of string
        while i < n and s[i].isdigit():
            num_str += s[i]
            i += 1

        # Convert the number string to an int
        count = int(num_str)

        # Append the decoded run
        decoded.append(char * count)

    return "".join(decoded)
