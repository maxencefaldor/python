def can_segment(s, word_set):
    """
    Solves the Word Break problem using Dynamic Programming.
    """
    n = len(s)

    # dp[i] will be True if the substring s[0...i-1] (length i)
    # can be segmented.
    # dp[0] is for the empty string, which is True by definition.
    dp = [False] * (n + 1)
    dp[0] = True

    # i represents the *end* of the substring we are checking
    for i in range(1, n + 1):
        # j represents a potential *start* of a word ending at i
        for j in range(i):
            # We can segment s[0...i-1] if:
            # 1. We could segment s[0...j-1] (which is dp[j])
            # 2. The remaining part s[j...i-1] is a valid word

            substring = s[j:i]

            if dp[j] and (substring in word_set):
                # We found a valid segmentation
                dp[i] = True
                # No need to check other j's for this i
                break

    # The final answer is whether the *entire* string (length n)
    # can be segmented.
    return dp[n]
