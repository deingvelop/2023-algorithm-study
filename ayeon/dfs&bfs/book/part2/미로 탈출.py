# N X M 직사각형
# (1,1) -> (N,M)
# 괴물 있는 부분 0, 없는 부분 1
# 탈출하기 위해 움직여야 하는 최소 칸의 개수

from collections import deque
N, M = map(int,input().split())
maze = [ list(map(int, input())) for _ in range(N) ]

visited = [ [ False  for _ in range(M) ] for _ in range(N) ]

def bfs(visited):

    queue = deque([[0,0]])
    visited[0][0] = True
    move = 1

    while queue:
    
        nx, ny= queue.popleft()
        move = maze[nx][ny] +1
        
        flag = False
        if nx > 0 and maze[nx-1][ny] != 0 and not visited[nx-1][ny]:
            queue.append([nx-1, ny])
            visited[nx-1][ny] = True
            maze[nx-1][ny] = move

        if nx < N-1 and maze[nx+1][ny] != 0 and not visited[nx+1][ny]:
            queue.append([nx+1, ny])
            visited[nx+1][ny] = True
            maze[nx+1][ny] = move

        if ny > 0 and maze[nx][ny-1] != 0 and not visited[nx][ny-1]:
            queue.append([nx, ny-1])
            visited[nx][ny-1] = True
            maze[nx][ny-1] = move

        if ny < M-1 and maze[nx][ny+1] != 0 and not visited[nx][ny+1]:         
            queue.append([nx, ny+1])
            visited[nx][ny+1] = True
            maze[nx][ny+1] = move 

    return maze[N-1][M-1]
        

print(bfs(visited))

for m in maze:
    print(m)
