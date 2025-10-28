def roman_to_int(s):
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0
    i = 0

    while i < len(s):
        # Get the value of the current character
        current_val = roman_map[s[i]]

        # Check if there is a next character and if it's larger
        if i + 1 < len(s) and roman_map[s[i + 1]] > current_val:
            # This is a subtractive case (e.g., "IV", "CM")
            total += roman_map[s[i + 1]] - current_val
            i += 2  # Move past both characters
        else:
            # This is an additive case (e.g., "VI", "III")
            total += current_val
            i += 1  # Move past one character

    return total
