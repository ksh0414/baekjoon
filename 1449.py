import sys
input = sys.stdin.readline

N, L = map(int, input().split())
spots = list(map(int, input().split()))
spots.sort()


now = 0
total = 0
for spot in spots:
    if now <= spot:
        now = spot + L
        total += 1
print(total)