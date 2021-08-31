n = int(input())
num_list = set()
nums = (1, 5, 10, 50)
def dfs(i, x, idx):
    if i == n:
        num_list.add(x)
        return
    else:
        for y in range(idx, 4):
            dfs(i+1, x+nums[y], y)
dfs(0, 0, 0)
print(len(num_list))