def is_arithmetic(n):
    n = str(n)
    if len(n) <= 1:
        return True
    criterion = int(n[1]) - int(n[0])
    for i in range(2, len(n)):
        sub = int(n[i]) - int(n[i-1])
        if sub != criterion:
            return False
    return True
n = int(input())
ans = 0
for i in range(1, n+1):
    if is_arithmetic(i):
        ans += 1
print(ans)