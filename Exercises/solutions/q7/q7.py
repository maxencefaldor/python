def count_palindromes(start, end):
    count = 0
    for i in range(start, end+1):
        if str(i) == str(i)[::-1]:
            count = count + 1
    return count
    
    
# Alternate solution
def count_palindromes_v2(start, end):
    return len([i for i in range(start, end+1) if str(i) == str(i)[::-1]])