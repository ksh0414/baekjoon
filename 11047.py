import sys
input = sys.stdin.readline

n, target = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

ans = 0
for coin in coins[::-1]:
    quotient = target // coin
    target -= quotient*coin
    ans += quotient
    if target == 0:
        break
print(ans)