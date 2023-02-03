# 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산

from collections import deque

n = int(input())
n1, n2 = map(int, input().split())
m = int(input())
relations = [ [] for _ in range(n+1) ]

for i in range(m):
    x, y = map(int, input().split())
    relations[x].append(y) # x부모 y자식
    relations[y].append(x) # y자식 x부모

q = deque([])
visited = [False]*(n+1)

def bfs(node, target):
    q.append([node,0]) # (인덱스, 촌수)
    visited[node] = True

    while q:
        cur = q.popleft() # 현재 노드
        for child in relations[cur[0]]: # 현재 노드의 연결관계
            if not visited[child]:
                if child == target:
                    return cur[1] + 1
                q.append([child, cur[1]+1])
                visited[child] = True
    
    return -1

print(bfs(n1, n2))
