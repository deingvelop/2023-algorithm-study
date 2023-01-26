import math
import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
road = [ [] for _ in range(N+1) ]

# 도로 정보 입력:
for _ in range(M):
    a,b = map(int, input().split())
    road[a].append(b)

short_path = [ math.inf for _ in range(N+1) ]

short_path[X] = 0

def bfs(X, K):
    answer = []

    queue = deque([X])
    short_path[X] = 0 # 방문

    while queue:
        q = queue.popleft()
        
        q_road = road[q]

        for r in q_road:
            start, end = r

            if short_path[end] == math.inf:
                short_path[end] = short_path[start] + 1 # 방문

            queue.append(end)
    
    for idx, val in enumerate(short_path):
        if val == K:
            answer.append(idx)

    if len(answer) == 0:
        print(-1)
    else:
        for a in answer:
            print(a)
    return 
            
bfs(X,K)
