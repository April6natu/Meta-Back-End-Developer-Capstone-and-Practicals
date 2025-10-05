# Algorithms for a Palindrome

def is_palindrome(str):
    startIndex = 0
    endIndex = len(str) - 1
    
    while startIndex < endIndex:
        if str[startIndex] != str[endIndex]:
            return False
        startIndex += 1
        endIndex -= 1
    
    return True
    
print(is_palindrome("racecars"))
print(is_palindrome("racecar"))
print(is_palindrome("madam"))
print(is_palindrome("hello"))
print(is_palindrome("a"))