# Determine if a string is a palindrome
# Should handle case sensitivity, spaces, even and odd number of characters
# Punctuation should be ignored

def is_palindrome(phrase):
    filtered = ''.join([c.lower() for c in phrase if c.isalnum()])
    for i in range(int(len(filtered)/2)):
        if filtered[i] != filtered[len(filtered)-1-i]:
            return False

    return True


if __name__ == '__main__':
    # Not a palindrome
    assert(False == is_palindrome('abcdef'))

    # Palindrome with odd number of characters
    assert(True == is_palindrome('Racecar'))

    # Palindrome with even number of characters
    assert(True == is_palindrome('abccba'))

    # Palindrome with spaces and punctuation
    assert(True == is_palindrome('A man, a plan, a canal... Panama!'))
