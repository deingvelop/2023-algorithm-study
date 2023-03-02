def find_parent(parent, x):
    #루트 노드를 찾을 때까지 재귀 호출
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
        
n, m = map(int, input().split())

parent = [0] * (n + 1) #부모 테이블 초기화하기
for i in range(1, n+1): #부모 테이블상에서, 부모를 자기 자신으로 초기화
    parent[i] = i
        
for i in range(m):
  op, a, b = map(int, input().split())
  if op == 0: #op가 0이면 '팀 합치기' > Union 연산
    union_parent(parent, a, b)
  else: #op가 1이면 '같은 팀 여부 확인' > Find 연산
    if find_parent(parent, a) == find_parent(parent, b): #부모가 같으면 YES 출력
      print('YES')
    else:
      print('NO')        
