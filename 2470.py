import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()
start = 0
end = n-1

min_value = 2*(10**9)
while start < end:
    sum_liquid = data[start] + data[end]
    if min_value > abs(sum_liquid):
        min_value = abs(sum_liquid)
        ans = (data[start], data[end])
    if sum_liquid > 0:
        end -= 1
    elif sum_liquid < 0:
        start += 1
    else:
        break
print(*ans)