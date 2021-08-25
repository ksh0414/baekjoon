#https://acmicpc.net/problem/11399
from itertools import accumulate

n = int(input())
data = list(map(int, input().split()))
print(sum(accumulate(sorted(data))))