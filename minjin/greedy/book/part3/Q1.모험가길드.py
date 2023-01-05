# # 풀이 1
n = int(input())
adventurer = list(map(int, input().split()))

groups = []

while adventurer:
    min_adventurer = min(adventurer)

    tmp = [min_adventurer]
    adventurer.remove(min_adventurer)

    while adventurer and max(tmp) > len(tmp):
        next_min = min(adventurer)
        tmp.append(next_min)
        adventurer.remove(next_min)

    if max(tmp) <= len(tmp):
        groups.append(tmp)

print(len(groups))


# 풀이 2 - 시간복잡도 개선 (min 대신 sort 사용)
n = int(input())
adventurer = list(map(int, input().split()))
adventurer.sort()

total_groups = 0
adv_cnt = 0

for adv in adventurer:
    adv_cnt += 1
    if adv_cnt >= adv:
        total_groups += 1
        adv_cnt = 0

print(total_groups)