x = int(input())
dp = [i for i in range(x+1)]

for i in range(4, x+1):
    for j in range(2, int(i**0.5)+1):
        if dp[i] > dp[i-j**2]+1:
            dp[i] = dp[i-j**2]+1
print(dp[x])