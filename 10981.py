INF = int(1e9)

def tsp(D):
    n = len(D)
    ans = INF
    VISITED_ALL = (1<<n)-1

    def find_path(start, last, visited, total):
        nonlocal ans
        if visited == VISITED_ALL:
            tmp = D[last][start] or INF
            ans = min(ans, total+tmp)
            return
        
        for city in range(n):
            if visited & (1<<city) == 0 and D[last][city] != 0:
                find_path(start, city, visited|(1<<city), total+D[last][city])
    
    for c in range(n):
        find_path(c, c, 1<<c, 0)
    
    return ans

graph = []
for _ in range(int(input())):
    graph.append(list(map(int, input().split())))
print(tsp(graph))