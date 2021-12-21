# P01_Valid_Palindrome.py
# 유효한 팰린드롬 문제
import collections

"""
문제 : 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며,
영문자와 숫자만을 대상으로 한다.


예제 1)
-입력 :
"A man, a plan, a canal : Panama"

-출력 :
"true"
"""
#펠린드롬 판별 함수

#1 리스트로 반환
def isPalindrome(s:str) -> bool:
    strs = []
    for char in s:
        if char.isalnum(): # 영문자, 숫자 제외하고 제거
            strs.append(char.lower()) # 모두 소문자로 변경해 리스트에 저장

    #펠린드롬 여부 판별
    while len(strs) > 1 :
        if strs.pop(0) != strs.pop():
            return False

    return True
test : str = "A man, a plan, a canal : Panama"
print(isPalindrome(test))
#------------------------------------------------------------------------------------

#2 데크 자료형을 이용한 최적화
from collections import deque
def isPalindrome2(s:str) -> bool:
    #자료형 데크로 선언
    strs = deque()
    for char in s:
        if char.isalnum(): # 영문자, 숫자 제외하고 제거
            strs.append(char.lower()) # 모두 소문자로 변경해 리스트에 저장

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True
print(isPalindrome2("A man, a plan, a canal : Panama"))
#------------------------------------------------------------------------------------

#3 슬라이싱 사용
import re
def isPalindrome3(s: str) ->bool:
    s = s.lower()
    #정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]

print(isPalindrome("A man, a plan, a canal : Panama"))