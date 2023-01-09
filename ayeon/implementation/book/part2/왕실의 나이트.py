init = input()

# L R U D
dx = [ 0, 0, -1, 1 ]
dy = [ -1, 1, 0, 0 ]

moves = []
# LLU LLD DDL DDR
# RRU RRD UUL UUR

for i in range(2):
    ddx = 0
    ddy = 0 

    ddx += dx[i]*2
    ddy += dy[i]*2

    for j in range(2, 4):
        moves.append((ddx+ dx[j], ddy +dy[j]))
        
for i in range(2):
    ddx = 0
    ddy = 0 

    ddx += dx[i]
    ddy += dy[i]

    for j in range(2, 4):
        moves.append((ddx+ dx[j]*2, ddy +dy[j]*2))

answer = 0

for move in moves:
    nx = ord(init[0])-96 + move[0] # 'a' = 97
    ny = int(init[1]) + move[1]
    if nx > 0 and nx < 9 and ny > 0 and ny < 9 :
        answer +=1

print(answer)
