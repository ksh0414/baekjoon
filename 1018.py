LINE = ('BW'*4, 'WB'*4)

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())

dp = [[8]*(M-7) for _ in range(N)]

for i in range(N):
    for j in range(M-7):
        for m in range(2):
            tmp = 0
            for k in range(8):
                if board[i][j+k] != LINE[j%2+m][k]:
                    tmp += 1
            dp[i][j] = min(dp[i][j], tmp)
for z in dp:
    print(*z)
ans = 64
for i in range(N-7):
    for j in range(M-7):
        ans = min(ans, sum([dp[i+k][j] for k in range(8)]))
print(ans)