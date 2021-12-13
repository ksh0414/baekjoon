import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

n, m = map(int, input().split())
parents = [i for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union(parents, b, c)
    else:
        if find(parents, c) == find(parents, b):
            print('YES')
        else:
            print('NO')