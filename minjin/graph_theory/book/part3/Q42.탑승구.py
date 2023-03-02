import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


g = int(input())
p = int(input())
parent = [0] * (g+1)

for i in range(1, g+1):
    parent[i] = i

result = 0
for _ in range(p):
    data = find_parent(parent, int(input()))    # 현재 비행기의 탑승구의 루트 확인
    if data == 0:
        break
    union_parent(parent, data, data-1)
    result += 1

print(result)