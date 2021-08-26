INF = int(1e9)

n = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))
total_distance = sum(roads)
min_cost = INF
ans = 0
for price, distance in zip(cities, roads):
    if min_cost > price:
        min_cost = price
    ans += min_cost*distance
print(ans)