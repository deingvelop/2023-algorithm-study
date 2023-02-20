#정확한 순위
#도달 가능하면 순위 측정가능
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*(n+1) for i in range(n+1)]

#자기자신 0으로 초기화
for i in range(1, n+1):
  graph[i][i] = 0

#각 간선에 대한 정보 입력받기
for _ in range(m):
  a, b = map(int,input().split())
  graph[a][b] = 1

#점화식에 따라 프로이드 워셜 알고리즘 실행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = 0
#도달 가능한지 체크
#자기보다 성적 높은학생 수 + 성적 낮은학생 수 = 총 학생수 일 때 순위 알 수 있다.
for i in range(1, n+1):
  count = 0
  for j in range(1, n+1):
    if graph[i][j] != INF or graph[j][i] !=INF:
      count+=1
  if count == n:
    result +=1

print(result)