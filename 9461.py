arr = [0, 1, 1]
t = []
for _ in range(int(input())):
    t.append(int(input()))
for i in range(3, max(t)+1):
    arr.append(arr[i-2]+arr[i-3])
for x in t:
    print(arr[x])