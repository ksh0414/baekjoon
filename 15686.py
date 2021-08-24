import sys
from itertools import combinations
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
nodes = [[] for _ in range(3)]
BLANK, HOUSE, CHICKEN = 0, 1, 2
for r in range(n):
  line = list(map(int, input().split()))
  for c in range(n):
    nodes[line[c]].append((r, c))

ans = INF
for chicken in combinations(nodes[CHICKEN], m):
  tmp = 0
  for house_r, house_c in nodes[HOUSE]:
    tmp += min([abs(house_r - c_r) + abs(house_c - c_c) for c_r, c_c in chicken])
    if ans < tmp:
      break
  else:
    ans = tmp #위 if에서 걸러지기 때문에 바로 업데이트
print(ans)