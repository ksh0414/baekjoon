def solve():
    arr = [True] * (end+1)
    arr[0] = arr[1] = False
    for i in range(2, int(end**0.5)+1):
        if arr[i]:
            j = 2
            while i*j <= end:
                arr[i*j] = False
                j += 1
    
    for x in [i for i in range(start, end+1) if arr[i]]:
        print(x)

start, end = map(int, input().split())
solve()