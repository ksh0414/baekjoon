n = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(set(nums))
order = {sorted_nums[i]: i for i in range(len(sorted_nums))}

for num in nums:
    print(order[num], end = ' ')