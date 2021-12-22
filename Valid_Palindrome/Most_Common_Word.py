#Most_Common_word.py

"""
04 가장 흔한 단어
금지된 단어를 제외한 가장 흔하게 등장하는 단어 출력. 대소문자 구분하지 않으며, 구두점(쉼표,마침표 등) 또한 무시

입력 :
paragraph = "Bob hit a ball, the hit Ball flew far after it was hit."
banned = ["hit"]

출력 :
"ball"
"""
from collections import Counter
import re

def most_common_word(s, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', s)\
            .lower().split()\
                if word not in banned]
    counts = Counter(words)
    return counts.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit Ball flew far after it was hit."
banned = ["hit"]
print(most_common_word(paragraph, banned))

