from collections import deque

n, m = map(int, input().split())
q = deque()
parent = [i for i in range(0, n+1)]
for _ in range(m):
    q.append(list(map(int, input().split())))


def union_parent(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


while q:
    op, a, b = q.popleft()
    if op == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")

