import sys
input = sys.stdin.readline

T = int(input())
while T:
    n, m = map(int, input().split())
    gold = []
    golds = list(map(int, input().split()))
    for i in range(0,n*m,m):
        gold.append(golds[i:i+m])

    global_max = 0
    # 첫번째 열
    for j in range(n):
        # DP
        d = [[0 for _ in range(m)] for _ in range(n)]
        
        # Start Point
        d[j][0] = gold[j][0]

        # [0][0] = 1
        for b in range(1, m):
            for a in range(n):
                if b-1 >= 0: # 왼쪽
                    d[a][b] = max(d[a][b-1] + gold[a][b], d[a][b])
                if a+1 < n and b-1 >= 0: # 왼쪽 아래
                    d[a][b] = max(d[a+1][b-1] + gold[a][b], d[a][b])
                if a-1 > 0 and b-1 >= 0: # 왼쪽 위
                    d[a][b] = max(d[a-1][b-1] + gold[a][b], d[a][b])

        local_max = 0
        for a in range(n):
            local_max = max(d[a][m-1], local_max)
        
        global_max = max(global_max, local_max)
    print(global_max)

    T-=1
