#combinations이 백트레킹보다 빠르다 원소가 적어서 그런가..?

import sys
from itertools import combinations
input = sys.stdin.readline
a = ord('a')

n, k = map(int, input().split())
if k < 5:
    print(0)
    exit(0)
elif k == 26:
    print(n)
    exit(0)

k -= 5
default = set('antic')
convert = {chr(a+i): 1 << i for i in range(26)}
words = []
check = set()
ans = 0
for _ in range(n):
    word = set(input().rstrip()) - default
    wl = len(word)
    if wl == 0:
        ans += 1
    elif wl <= k:
        tmp = 0
        for char in word:
            tmp += convert[char]
        words.append(tmp)
        check |= word

l = len(check)
check = map(lambda x: convert[x], check)
def compare(w):
    teach = sum(w)
    result = 0
    for word in words:
        if teach & word == word:
            result += 1
    return result
plus = max(map(compare, combinations(check, min(l,k))))
print(ans+plus)