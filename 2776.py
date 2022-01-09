import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    see_nums = set(map(int, input().split()))
    m = int(input())
    for x in map(int, input().split()):
        if x in see_nums:
            print('1')
        else:
            print('0')