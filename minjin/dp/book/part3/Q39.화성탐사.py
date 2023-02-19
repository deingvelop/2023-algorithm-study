## 시도 1 - 테케2만 계속 오류 남
# from collections import deque
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#
#     graph = []
#     for _ in range(n):
#         graph.append(list(map(int, input().split())))
#
#     answer = [[INF for _ in range(n)] for _ in range(n)]
#     def bfs(start):
#         dx = [-1, 1, 0, 0]
#         dy = [0, 0, -1, 1]
#
#         q = deque([start])
#         answer[0][0] = graph[0][0]
#
#         while q:
#             x, y = q.popleft()
#
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if 0 <= nx < n and 0 <= ny < n:
#                     if answer[nx][ny] == INF:
#                         q.append((nx, ny))
#                         answer[nx][ny] = answer[x][y] + graph[nx][ny]
#                     else:
#                         answer[nx][ny] = min(answer[x][y] + graph[nx][ny], answer[nx][ny])
#
#
#     bfs((0, 0))
#
#     print(answer[n-1][n-1])


# 시도 2 - 교재 살짝 참고 - 다익스트라
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

t = int(input())
for _ in range(t):
    n = int(input())

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    answer = [[INF for _ in range(n)] for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    pq = []
    heapq.heappush(pq, (graph[0][0], 0, 0))
    answer[0][0] = graph[0][0]

    while pq:
        so_far, x, y = heapq.heappop(pq)

        if answer[x][y] < so_far:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = so_far + graph[nx][ny]
                if new_cost < answer[nx][ny]:
                    answer[nx][ny] = new_cost
                    heapq.heappush(pq, (answer[nx][ny], nx, ny))

    print(answer[n-1][n-1])