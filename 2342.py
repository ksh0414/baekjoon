#dp를 생성하는 법 잘 기억해두자
data = list(map(int, input().split()))
data.pop()
data = [0] + data
ll = len(data)
if ll <= 1:
    print(ll*2)
    exit(0)
dp = [[[int(1e9)for _ in range(5)] for _ in range(5)]for _ in range(ll)] #cnt, l, r
dp[0][0][0] = 0
for i in range(1, ll):
    now = data[i]
    for l in range(5):
        for r in range(5):
            if l != now:
                plus = 0
                sub = abs(now - r)
                if r == 0:
                    plus = 2
                elif sub == 0:
                    plus = 1
                elif sub%2 == 0:
                    plus = 4
                else:
                    plus = 3
                dp[i][l][now] = min(dp[i][l][now], dp[i-1][l][r]+plus)
            if r != now:
                plus = 0
                sub = abs(now - l)
                if l == 0:
                    plus = 2
                elif sub == 0:
                    plus = 1
                elif sub%2 == 0:
                    plus = 4
                else:
                    plus = 3
                dp[i][now][r] = min(dp[i][now][r], dp[i-1][l][r]+plus)
print(min([min(dp[ll-1][i]) for i in range(5)]))