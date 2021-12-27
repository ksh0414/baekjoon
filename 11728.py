import sys

a, b = map(int, input().split())
arr = sys.stdin.read().split()

print(' '.join(sorted(arr, key=int)))