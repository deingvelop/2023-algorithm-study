# # 시도 1 - 테케는 모두 통과
#
# from collections import deque
# import sys
# input = sys.stdin.readline
#
# n, m, k, x = map(int, input().split())
# graph = [[0] * (n+1) for _ in range(n+1)]
# city_min_distance = {x: 0}
#
#
# for _ in range(m):
#     city1, city2 = map(int, input().split())
#     graph[city1][city2] = 1
#
#
# def dfs(start):
#     q = deque()
#     q.append(start)
#
#     while q:
#         now_city = q.popleft()
#         for another_city in range(1, n+1):
#             if graph[now_city][another_city] and another_city not in city_min_distance.keys():
#                 city_min_distance[another_city] = city_min_distance[now_city] + 1
#                 q.append(another_city)
#
#
# dfs(x)
#
# cnt = 0
# for i in range(1, n + 1):
#     if i != x and i in city_min_distance.keys() and city_min_distance[i] == k:
#         print(i)
#         cnt += 1
#
# if cnt == 0:
#     print(-1)

# 시도 2 - 인터넷 참고
from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)

for _ in range(m):
    city1, city2 = map(int, input().split())
    graph[city1].append(city2)      # 2차원 배열에다가, 각 그래프의 자식 노드들을 담음

answer = []

def bfs(start):
    q = deque([start])
    distance[start] = 0

    while q:
        now_city = q.popleft()
        for target_city in graph[now_city]:
            if distance[target_city] == -1:
                distance[target_city] = distance[now_city] + 1
                q.append(target_city)
                if distance[target_city] == k:
                    answer.append(target_city)


bfs(x)
if len(answer) == 0:
    print(-1)

else:
    answer.sort()
    for city in answer:
        print(city)

