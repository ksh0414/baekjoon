import sys
from collections import defaultdict
input = sys.stdin.readline

def sum_word(info):
    global words
    total = 0
    for exponent, chars in enumerate(words[1:], 0):
        if word == defaultdict(int):
            continue
        for char in chars.keys():
            total += (10**exponent)*info[char]*words[exponent+1][char]
    return total

def cal(info, idx):
    global words, ans
    print(idx)
    if idx <= 0 or len(info) >= 8:
        ans = max(ans, sum_word(info))
    chars = words[idx]
    if chars == defaultdict(int):
        return
    for char in chars.keys():
        print(char, info)
        if char not in info:
            info[char] = 9-len(info)
        if len(info) >= 8:
            break
        cal(info, idx-1)


ans = 0
words = [defaultdict(int) for _ in range(9)]
info = {}
for _ in range(int(input())):
    word = input().strip()
    for i, char in enumerate(word[::-1], 1):
        words[i][char] += 1
idx = 8
while words[idx] == defaultdict(int): idx -= 1
cal(info, idx)
print(ans)