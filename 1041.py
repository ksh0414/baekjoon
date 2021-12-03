N = int(input())
nums = list(map(int, input().split()))

def min_couple():
    tmp = []
    tmp.append([nums[1]+nums[2], nums[2]+nums[4], nums[3]+nums[4], nums[1]+nums[3]])
    tmp.append([nums[0]+nums[2], nums[2]+nums[5], nums[3]+nums[5], nums[0]+nums[3]])
    tmp.append([nums[0]+nums[1], nums[1]+nums[5], nums[4]+nums[5], nums[0]+nums[4]])
    tmp = tmp+list(reversed(tmp))
    return (min([min(tmp[i]) for i in range(3)]), min([nums[i]+min(tmp[i]) for i in range(6)]))

if N == 1:
    print(sum(nums)-max(nums))
else:
    min_1 = min(nums)
    min_2, min_3 = min_couple()
    ans = (((min_2+min_1*(N-2))*4)*(N-1))+((min_3+min_2*(N-2))*4)+(min_1*(N-2)*(N-2))
    print(ans)