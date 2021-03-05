def palindrome(word, idx):
    list_word = ''.join(reversed(list(word)))
    if list_word == word:
        return f'{word} is a palindrome'
    else:
        return f'{word} is not a palindrome'

print(palindrome('abcba', 0))