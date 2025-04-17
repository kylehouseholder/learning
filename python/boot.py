from functools import lru_cache

@lru_cache()
def is_palindrome(word):
    if word[0] == word[-1]:
        newWord = word
        if is_palindrome(word[1:-2]):
            return True
