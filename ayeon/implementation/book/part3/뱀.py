from collections import deque

N = int(input()) # 보드의 크기
K = int(input()) # 사과의 개수

board = [ [ 0 for _ in range(N) ] for _ in range(N) ]

for i in range(K):  # 사과의 위치
    x, y = map(int, input().split())
    board[x-1][y-1] = 1 # 사과 x-1 행 y-1 열

rotations = deque()
L = int(input()) # 방향 변환 횟수
for i in range(L):
    X, C = input().split()
    rotations.append([int(X), C])

# L (왼쪽으로 90 회전)
# R (오른쪽으로 90 회전)

answer = 0 # 게임이 몇 초에 끝

x, y = 0, 0 # 뱀의 위치 (head)
r = 0 # 오른쪽 

# R U L D

# dx = [ 1, 0, -1, 0 ]
# dy = [ 0, -1, 0, 1 ]

dx = [ 0, -1, 0, 1 ]
dy = [ 1, 0, -1, 0 ]

def left(r) :
    if r == 3:
        return 0
    return r+1

def right(r) :
    if r == 0:
        return 3
    return r-1

board[x][y] = 2 # 뱀 2

snake = deque()
snake.append([x,y])


while True:
    answer += 1
    
    # 1. 몸길이를 늘려 머리를 다음칸
    x += dx[r]
    y += dy[r]

    # 벽
    if x < 0 or x >= N or y < 0 or y >= N:
        break
    
    # 뱀
    if board[x][y] == 2:
        break

    snake.append([x, y])

    # 2. 사과가 있다면, 사과를 먹는다. 꼬리 움직이지 않는다
    if board[x][y] == 1:
        board[x][y] = 2
    else:
        # 3. 사과 없다면, 꼬리를 한칸 비워준다.
        board[x][y] = 2
        tail_x, tail_y = snake.popleft()
        board[tail_x][tail_y] = 0

    # 방향
    if len(rotations)>0 and rotations[0][0] == answer:
        X, C = rotations.popleft()
        if C == 'L':
            r = left(r)
        else:
            r = right(r)

    # print("t:", answer)
    # for b in board:
    #     print(b)

print(answer)
