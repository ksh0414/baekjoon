def upper_bound(start, end, k):
    while start < end:
        mid = (start+end) // 2
        if data[mid] <= k:
            start = mid+1
        else:
            end = mid
    return end

def solve():
    start, end = 0, data[-1]
    ans = 0
    while start <= end:
        mid = (start+end) // 2
        h_idx= upper_bound(0, l, mid)
        total = sum([x-mid for x in data[h_idx:]])
        if total >= m:
            ans = mid
            start = mid+1
        else:
            end = mid-1
    return ans
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
l = len(data)
print(solve())