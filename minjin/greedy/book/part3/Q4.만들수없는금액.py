# 풀이 1 - (greedy x, 완탐) itertools 활용
import itertools

n = int(input())
coins = list(map(int, input().split()))
can_make = []

for i in range(1, n+1):
    made_tuples = itertools.permutations(coins, i)
    for tuple in made_tuples:
        if sum(tuple) not in can_make:
            can_make.append(sum(tuple))
can_make.sort()

check_num = 1
while True:
    if check_num not in can_make:
        break
    check_num += 1

print(check_num)


# 풀이 2 - greedy. 교재
n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for coin in coins:
    if target < coin:
        break
    target += coin

print(target)