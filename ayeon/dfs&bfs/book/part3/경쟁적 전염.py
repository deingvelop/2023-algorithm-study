# N X N 시험관
# 바이러스는 1번부터 K번까지

# 1초마다, 상, 하, 좌, 우
# 단, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다.
# 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.

# S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류
# X와 Y는 각각 행과 열
# 바이러스가 존재하지 않는다면, 0을 출력

from collections import deque

q = deque() # 1초 지날 때 증식한 바이러스의 새로운 위치

# input
N, K = map(int, input().split())
tube = [ list(map(int, input().split())) for _ in range(N) ]
S, X, Y = map(int, input().split())

# 초기 바이러스 위치
virus = [ [ ] for _ in range(K+1) ]

for i in range(N):
    for j in range(N):
        if tube[i][j] > 0:
            k = tube[i][j]
            virus[k].append([i,j,k]) # (i,j) 에 k번 바이러스

for vir in virus:
    for v in vir:
        q.append(v) # 번호가 작은 바이러스부터 q에 삽입

time = 0
while time < S:
    nq = deque() # 다음 차례에 사용할 q
    
    while len(q) > 0 :
        i, j, k = q.popleft()  # (i,j) 에 k번 바이러스
        # tube[i][j] = k

        if i>0 and tube[i-1][j] == 0:
            tube[i-1][j] = k
            nq.append([i-1,j,k])
        if j>0 and tube[i][j-1] == 0:
            tube[i][j-1] = k
            nq.append([i,j-1,k])
        if i<N-1 and tube[i+1][j] == 0:
            tube[i+1][j] = k
            nq.append([i+1,j,k])
        if j<N-1 and tube[i][j+1] == 0:
            tube[i][j+1] = k
            nq.append([i,j+1,k])
    
    q.extend(nq)
    time += 1

print(tube[X-1][Y-1])
