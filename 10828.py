import sys
input = sys.stdin.readline
COMMAND, NUM = 0, 1

stk = [-1]
for _ in range(int(input())):
    case = list(input().rstrip().split())
    if case[COMMAND] == 'push':
        stk.append(case[NUM])
    elif case[0] == 'pop':
        if len(stk) == 1:
            print(-1)
        else:
            print(stk.pop())
    elif case[0] == 'size':
        print(len(stk)-1)
    elif case[0] == 'empty':
        print(1 if len(stk) == 1 else 0)
    else:
        print(stk[-1])