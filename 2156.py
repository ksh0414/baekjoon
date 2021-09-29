import sys
input = sys.stdin.readline

N = int(input())
a = [0, int(input()), 0]
for _ in range(N-1):
    wine = int(input())
    tmp= max(a)
    a[2] = a[1]+wine
    a[1] = a[0]+wine
    a[0] = tmp
print(max(a))