def Palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return Palindrome(text[1:-1])


print(Palindrome("level"))