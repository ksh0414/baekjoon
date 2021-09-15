#트리에서의 dp 중요... dp 잘 공부하자
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
EARLY, NOT_EARLY = 0, 1

def dfs(now):
    global visited, dp
    dp[now][EARLY] = 1
    visited[now] = True
    for n_n in tree[now]:
        if not visited[n_n]:
            dfs(n_n)
            dp[now][EARLY] += min(dp[n_n])
            dp[now][NOT_EARLY] += dp[n_n][EARLY]

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)
dfs(1)
print(min(dp[1]))