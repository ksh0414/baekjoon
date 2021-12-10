#dict를 이용하는게 훨씬 빠르다
#해당 시행 도중의 과정이 결과에 영향을 미치면 안된다.
from collections import defaultdict

WEIGHT, VALUE = 0, 1
N, K = map(int, input().split())

data = []
dp = defaultdict(int)
dp[0] = 0
for _ in range(N):
    x_w, x_v = map(int, input().split())
    items = tuple(dp.items())
    tmp = {}
    for w, v in items:
        if x_w+w <= K:
            tmp[x_w+w] = max(dp[x_w+w], dp[w]+x_v)
    dp.update(tmp)
print(max(dp.values()))