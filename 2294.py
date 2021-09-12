import sys
input = sys.stdin.readline

coins = []
n, k = map(int, input().split())
dp = [k+1] * (k+1)
for _ in range(n):
    try:
        x = int(input())
        dp[x] = 1
        coins.append(x)
    except:
        continue

coins.sort()
for i in range(coins[0]*2, k+1):
    for x in coins:
        if dp[i] > dp[i-x] + 1:
            dp[i] = dp[i-x]+1
print(dp[k] if dp[k] <= k else -1)