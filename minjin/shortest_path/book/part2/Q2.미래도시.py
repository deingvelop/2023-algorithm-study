import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())  # n = 노드, m = 간선
connection = [[] for _ in range(n + 1)]

for _ in range(m):
    node1, node2 = map(int, input().split())
    connection[node1].append(node2)
    connection[node2].append(node1)

x, k = map(int, input().split())  # 목적지 = x, 소개팅 장소 = k

dist_info = [(INF, False) for _ in range(n+1)]
q = deque([])
visited = [False] * (n+1)

def find_shortest(start):
    q.append(start)
    if start == k:
        dist_info[start] = (0, True)
    else:
        dist_info[start] = (0, False)

    while q:
        now = q.popleft()
        so_far, already_met = dist_info[now]
        visited[now] = True
        for con in connection[now]:
            so_far_con, already_met_con = dist_info[con]
            if con == k or already_met_con:
                already_met = True
            if already_met and so_far_con < (so_far + 1):
                d = so_far + 1
            else:
                d = min((so_far+1), so_far_con)
            dist_info[con] = (d, already_met)
            if visited[con] == False:
                q.append(con)

    if dist_info[x][1] == False:
        return -1
    else:
        return dist_info[x][0]


print(find_shortest(1))