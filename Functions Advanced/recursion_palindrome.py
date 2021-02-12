def palindrome(text, index):
    if index == len(text) // 2:
        return f"{text} is a palindrome"

    if text[index] == text[-index - 1]:
        return palindrome(text, index + 1)
    else:
        return f"{text} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
