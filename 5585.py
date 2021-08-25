change = 1000 - int(input())
ans = 0
for x in (500, 100, 50, 10, 5, 1):
    quotient = change//x
    change -= quotient*x
    ans += quotient
print(ans)
