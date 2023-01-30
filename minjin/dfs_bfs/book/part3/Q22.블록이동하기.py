# # 시도 1 - 회전에 대한 고려 X - 당연히 실패
# from collections import deque
#
# def solution(board):
#
#     n = len(board)
#     answer = 0
#     x, y = 0, 1
#     q = deque([(x, y)])
#
#     board[0][0] = 1
#     board[0][1] = 1
#
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     while q:
#         now_x, now_y = q.popleft()
#         for i in range(4):
#             nx = now_x + dx[i]
#             ny = now_y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
#                 answer += 1
#                 board[nx][ny] = board[now_x][now_y] + 1
#
#     return answer
#

# 정답 - 인터넷 참고 풀이
from collections import deque


def can_move(cur1, cur2, new_board):
    Y, X = 0, 1
    moves = []

    # 평행이동
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dy, dx in directions:
        nxt1 = (cur1[Y] + dy, cur1[X] + dx)
        nxt2 = (cur2[Y] + dy, cur2[X] + dx)
        if new_board[nxt1[Y]][nxt1[X]] == 0 and new_board[nxt2[Y]][nxt2[X]] == 0:
            moves.append((nxt1, nxt2))

    # 가로방향 일 때 회전
    if cur1[Y] == cur2[Y]:
        UP, DOWN = -1, 1
        for d in [UP, DOWN]:
            if new_board[cur1[Y] + d][cur1[X]] == 0 and new_board[cur2[Y] + d][cur2[X]] == 0:
                moves.append((cur1, (cur1[Y] + d, cur1[X])))
                moves.append((cur2, (cur2[Y] + d, cur2[X])))

    # 세로 방향 일 때 회전
    else:
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            if new_board[cur1[Y]][cur1[X] + d] == 0 and new_board[cur2[Y]][cur2[X] + d] == 0:
                moves.append(((cur1[Y], cur1[X] + d), cur1))
                moves.append(((cur2[Y], cur2[X] + d), cur2))

    return moves


def solution(board):

    # board 외벽 둘러싸기
    N = len(board)
    new_board = [[1] * (N + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            new_board[i + 1][j + 1] = board[i][j]

    # 현재 좌표 위치 큐 삽입, 확인용 set
    q = deque([((1, 1), (1, 2), 0)])
    confirm = set([((1, 1), (1, 2))])

    while q:
        cur1, cur2, count = q.popleft()
        if cur1 == (N, N) or cur2 == (N, N):
            return count
        for nxt in can_move(cur1, cur2, new_board):
            if nxt not in confirm:
                q.append((*nxt, count + 1))
                confirm.add(nxt)