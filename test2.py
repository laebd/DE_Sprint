import re
import string


def is_palindrome(text):
    pat = f"[\s{re.escape(string.punctuation)}]"
    text = re.sub(pat, "", text).lower()
    return text == text[::-1]

is_palindrome("fdfdfdfsf") 
is_palindrome("abba abba")  