#Reverse_string
"""
02 문자열 뒤집기
문자열 뒤집는 함수 작성, 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작.

입력:
["h", "e", "l", "l", "o"]
출력:
["O", "l", "l", "e", "h"]
"""
def reverse_string(s):
    s= list(s)
    print(id(s))
    left, right = 0, len(s)-1
    while left < right :
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    print(s)
strs = "hello"
reverse_string(strs)
#-----------------------------------------------------------------

# revers()함수 사용
def reverseString(s):
    s = list(s)
    s.reverse()
    print(s)
reverseString(strs)
#-----------------------------------------------------------------