import sys
input = sys.stdin.readline

stk = []
for _ in range(int(input())):
    x = int(input())
    if x:   stk.append(x)
    else:   stk.pop()
print(sum(stk))