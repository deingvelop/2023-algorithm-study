#bfs로 바로 옆 국가 국경선 여는것 까지는 구현..(문제는 인접한 모든 국가의 국경선을 열어야했음)
from collections import deque

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0] # 행
dy = [0, 1, 0, -1] # 열

result = 0

# 특정 위치에서 출발해 모든 연합을 체크한 뒤에 데이터 갱신

def process(x, y, index):
    # (x, y)의 위치와 연결된 연합 정보를 담는 리스트
    united = []
    united.append((x, y))
    # 너비 우선 탐색을 위한 큐 자료구조 정의
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합 수
    
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라 확인해서 -1이라면
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny]== -1:
                if l<= abs(graph[nx][ny] - graph[x][y]) <=r:
                    q.append((nx, ny)) # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count+=1
                    united.append((nx, ny))
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count    
        
        
total_count = 0
# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: #해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n * n: # union의 모든 index가 순차적으로 들어가야만 break가 되겠구나...
        break   
    total_count += 1
print(total_count)