n, m = map(int, input().split())
now_y, now_x, d = map(int, input().split())
map = []
for i in range(m):
    map.append(input().split())
map[now_x][now_y] = 1

dir_check = 0
game_continue = True
answer = 1

d_ver = [-1, 0, 1, 0]
d_hor = [0, 1, 0, -1]

# 네 방향 다 확인 - 네 방향 다 못 가면 뒤로 후진
while game_continue:
    while dir_check < 4:
        d = (d + 3) % 4
        tmp_x, tmp_y = now_x + d_hor[d], now_y + d_ver[d]
        if 0 <= tmp_x < n and 0 <= tmp_y < m and map[tmp_y][tmp_x] == '0':
            answer += 1
            map[tmp_y][tmp_x] = '1'
            now_x, now_y = tmp_x, tmp_y
            dir_check = 0
        dir_check += 1
    else:
        d -= 2
        tmp_x, tmp_y = now_x + d_hor[d], now_y + d_hor[d]
        if map[tmp_y][tmp_x] != '0':
            game_continue = False

print(answer)