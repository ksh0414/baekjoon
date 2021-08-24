n = int(input())
data = list(map(int, input().split()))

stk = []
ans = [0] * n
for i in range(n-1, -1, -1):
    while stk and stk[-1][0] < data[i]:
        _, idx = stk.pop()
        ans[idx] = i+1
    stk.append((data[i], i))

print(*ans)