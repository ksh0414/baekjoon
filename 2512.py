import sys
from itertools import accumulate
from bisect import bisect
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort() #bisect를 위해 오름차순으로 정렬
acc_data = list(accumulate(data)) #누산기를 사용하여 index별 합계 저장
acc_data = [0] + acc_data #bisect를 사용해 index를 구하기 때문에 mid<data[0]일 경우 합계는 0
total_budget = int(input())
max_budget = max(data)

if sum(data) > total_budget:
    start = 0
    end = max_budget
    while(start<end):
        mid = (start+end)//2
        max_idx = bisect(data, mid)
        now_sum = acc_data[max_idx]+(n-max_idx)*mid
        if now_sum > total_budget:
            end = mid
        else:
            start = mid+1
            max_budget = mid
    
print(max_budget)
        