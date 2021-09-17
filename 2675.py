import sys
input = sys.stdin.readline

for _ in range(int(input())):
    string = input().rstrip()
    for x in string[2:]:
        print(x*int(string[0]), end = '')
    print()