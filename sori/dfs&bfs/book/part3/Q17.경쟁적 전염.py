from collections import deque

n, k = map(int, input().split())
graph = [] # 전체 보드 정보를 담는 리스트
virus = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            virus.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
virus.sort()
queue = deque(virus)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색 진행
while queue:
    virus, s, x, y = queue.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if target_s == s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])

#풀이법은 생각 하긴 했지만 제대로 구현하지 못함.
#바이러스가 들어있는 좌료와 시간, 바이러스값을 한번에 넣으면 쉽게 해결 가능