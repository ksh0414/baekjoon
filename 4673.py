def sum(x):
    result = x
    while x > 0:
        result += x%10
        x //= 10
    return result

nums = set()
for i in range(1, 10001):
    if i not in nums:
        print(i)
    nums.add(sum(i))