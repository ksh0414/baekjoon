import sys
input = sys.stdin.readline

ans = 0
for _ in range(int(input())):
    string = input().rstrip()
    pre_char = {string[0]}
    pre = string[0]
    for char in string[1:]:
        if pre == char:
            continue

        if char in pre_char:
            break
        pre_char.add(char)
        pre 
        ans += 1
print(ans)