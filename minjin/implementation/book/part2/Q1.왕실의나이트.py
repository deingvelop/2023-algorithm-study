alphabet_dict = ["a", "b", "c", "d", "e", "f", "g", "h"]
map = [[True for _ in range(8)] for _ in range(8)]

s_input = input()
now_x, now_y = alphabet_dict.index(s_input[0]), int(s_input[1]) - 1
cnt = 0

hor_move = [2, 2, -2, -2, 1, 1, -1, -1]
ver_move = [1, -1, 1, -1, 2, -2, 2, -2]

for i in range(8):
    if 0 <= now_x + hor_move[i] <= 7 and 0 <= now_y + ver_move[i] <= 7:
        cnt += 1

print(cnt)