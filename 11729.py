import sys
sys.setrecursionlimit(10**8)

def hanoi(n, from_pos, tmp_pos, to_pos):
    global ans, result
    if n == 1:
        ans += 1
        result.append((from_pos, to_pos))
        return
    hanoi(n-1, from_pos, to_pos, tmp_pos)
    result.append((from_pos, to_pos))
    ans += 1
    hanoi(n-1, tmp_pos, from_pos, to_pos)

ans = 0
result = []
hanoi(int(input()), 1, 2, 3)
print(ans)
for line in result:
    print(*line)