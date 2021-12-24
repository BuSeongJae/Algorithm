#Longest_Palindrome_Substring.py

"""
가장 긴 팰린드롬 문자열 출력

입력:
"babad"

출력:
"bab" or "aba"

예제2)
입력:
"cbbd"
출력:
"bb"
"""
from collections import deque
def longest_Palindrome(s):
    def expand(left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    if len(s) < 2 or s== s[::-1]:
        return s
    result = ''
    for i in range(len(s)-1):
        result = max(result,
                     expand(i, i+1),
                     expand(i, i+2),
                     key = len)
    return result



print(longest_Palindrome("babad"))
print(longest_Palindrome("cbbdf"))
