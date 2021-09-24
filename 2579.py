import sys
input = sys.stdin.readline
SCORE, COUNT = 0, 1
ONE, TWO = 0, 1

n = int(input())
dp = [[(0, 0), (0, 0)] for _ in range(n+1)]
stairs = [0]
for i in range(1, n+1):
    stairs.append(int(input()))

dp[1][ONE] = (stairs[1], 1)
for i in range(2, n+1):
    if dp[i-1][ONE][COUNT] <= 1:
        tmp = max(dp[i-1])
        dp[i][ONE] = (tmp[SCORE]+stairs[i], tmp[COUNT]+1)
    else:
        dp[i][ONE] = (dp[i-1][ONE]+stairs[i], dp[i-1][ONE][COUNT]+1)
    dp[i][TWO] = (max(dp[i-2])[SCORE]+stairs[i], 1)

print(max(dp[n])[SCORE])
