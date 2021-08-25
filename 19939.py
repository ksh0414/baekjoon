n, k = map(int, input().split())
min_value = k*(1+k)//2
if n < min_value:
    ans = -1
else:
    if (n-min_value) % k: #나머지가 있으면
        ans = k
    else: #나머지가 없으면
        ans = k-1
print(ans)