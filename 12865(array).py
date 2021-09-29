from collections import defaultdict

WEIGHT, VALUE = 0, 1
N, K = map(int, input().split())

data = []
dp = defaultdict(int)
dp[0] = 0
for _ in range(N):
    x_w, x_v = map(int, input().split())
    for w, v in dp.items():
        if x_w+w <= K:
            dp[x_w+w] = max(dp[x_w+w], dp[w]+x_v)
print(max(dp.values()))