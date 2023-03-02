import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())

parent = [ i for i in range(N+1) ]

for _ in range(M):
    t, a, b = map(int, input().split())

    if t == 0: # 팀 합치기
        union_parent(parent, a, b)

    else: # 같은 팀 여부 확인
        if find_parent(parent, a)  == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
