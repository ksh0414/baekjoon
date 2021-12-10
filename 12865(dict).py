#dict�� �̿��ϴ°� �ξ� ������
#�ش� ���� ������ ������ ����� ������ ��ġ�� �ȵȴ�.
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