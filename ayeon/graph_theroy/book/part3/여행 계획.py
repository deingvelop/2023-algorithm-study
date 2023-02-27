# 1~N 번까지의 번호로 구분
# 임의의 여행지 사이에는 두 여행지를 연결하는 도로 존재
# 도로는 양방향 이동 가능

# 여행지의 개수, 여행지 연결 정보 -> 여행 계획이 가능한지 여부 판별

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

parent = [ i for i in range(N+1) ]


def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a]) # parent[a] 재귀적 호출
    return parent[a]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# main
for i in range(N):
    c = list(map(int, input().split()))

    for j in range(N):
        if i < j and c[j] == 1: # 중복 제거
            print(i+1, j+1)
            union_parent(i+1, j+1) # 연결된 여행지
            

plan = list(map(int, input().split())) # 여행 계획

flag = True
p = find_parent(plan[0])

for i in plan:
    if p != find_parent(i):
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")

'''
INPUT > 

5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3

OUTPUT >

YES
'''
