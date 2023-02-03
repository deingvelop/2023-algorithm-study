import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # RecursionError

T = int(input())

dx = [ 0, 0, -1, 1]
dy = [ -1, 1, 0, 0]

def dfs(a, visited, x, y):
    if x > M-1 or y > N-1 or x < 0 or y < 0:
        return False
        
    if not visited[y][x] and a[y][x] == 1:
        visited[y][x] = True
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            dfs(a, visited, nx, ny) 

        return True

    return False

answers = []
while T > 0:
    M, N, K = map(int, input().split())
    
    a = [ [0 for _ in range(M)] for _ in range(N) ]
    visited = [ [False for _ in range(M)] for _ in range(N) ]
    for _ in range(K):
        X, Y = map(int, input().split())
        a[Y][X] = 1
    
    answer = 0
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and dfs(a, visited, j, i):
                answer += 1
    
    answers.append(answer)
    T -=1

for a in answers:
    print(a)
