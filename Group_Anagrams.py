#Group_Anagrams.py
"""
문자열 배열을 받아 에너그램 단위로 그룹핑
입력 :
["eat", "tea", "tan", "ate", "nat", "bat"]

출력:
[['eat', 'tea', 'ate'],
 ['tan', 'nat'],
 ['bat']]
"""
import collections


def group_anagrams(arr):
    arr = list(arr)
    anagrams = collections.defaultdict(list)

    for word in arr:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


arr =["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(arr))





arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
group_anagrams(arr)

