from itertools import combinations
import sys
input = sys.stdin.readline

def back_tracking(l, idx, cnt):
    global char_group
    if cnt == k:
        global ans
        tmp = 0
        for need_char in need_char_set:
            for char in need_char:
                if char not in char_group:
                    break
            else:
                tmp += 1
        ans = max(ans, tmp)
        return
    for j in range(idx, l):
        char_group.append(total_char[j])
        back_tracking(l, j+1, cnt+1)
        char_group.pop()

    

n, k = map(int, input().split())
ans = 0
need_char_set = []
total_char = set()
default = {'a', 'n', 't', 'i', 'c'}
char_group = []
for _ in range(n):
    tmp = set(input().rstrip())-default
    need_char_set.append(tmp)
    total_char.update(tmp)
    
if k < 5:
    pass
elif k-5 >= len(total_char):
    ans = n
else:
    l = len(total_char)
    total_char = list(total_char)
    back_tracking(l, 0, 5)
print(ans)