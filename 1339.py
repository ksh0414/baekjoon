import sys
from collections import defaultdict
input = sys.stdin.readline

char_weight = defaultdict(int)
for _ in range(int(input())):
    word = input().strip()
    for exponent, char in enumerate(word[::-1]):
        char_weight[char] += 10**exponent
char_order = list(sorted(char_weight.items(), key = lambda x:x[1], reverse = True))
ans = 0
num = 9
for char, weight in char_order:
    ans += num*weight
    num -= 1
print(ans)