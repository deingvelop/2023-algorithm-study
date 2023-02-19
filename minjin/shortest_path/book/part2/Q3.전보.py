import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
conn = [[] for _ in range(n+1)]
shortest_cost = [INF] * (n+1)
# last_reach = 0
# can_reach = []

for _ in range(m):
    x, y, z = map(int, input().split())
    conn[x].append((y, z))

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        so_far, now = heapq.heappop(pq)
        for target, cost in conn[now]:
            new_cost = so_far + cost
            if shortest_cost[target] < new_cost:
                continue
            else:
                shortest_cost[target] = new_cost
                heapq.heappush(pq, (new_cost, target))

dijkstra(c)

can_reach = 0
last_reach = 0
for c in shortest_cost:
    if c != INF:
        can_reach += 1
        last_reach = max(last_reach, c)

print(can_reach, last_reach)