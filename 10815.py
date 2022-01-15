import sys
input = sys.stdin.readline

n = int(input())
a = set(map(int, input().split()))
input()
for x in map(int, input().split()):
    if x in a:
        print(1, end = ' ')
    else:
        print(0, end = ' ')