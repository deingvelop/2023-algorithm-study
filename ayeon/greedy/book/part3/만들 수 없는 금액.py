from itertools import combinations

N = int(input())
arr = list(map(int, input().split()))

coins = set(arr.copy())

for i in range(2, len(arr)+1):
    com = list(combinations(arr,i)) # 순열
    for c in com:
        coins.add(sum(c)) # 순열의 합
answer = 1

for i in coins:
    if i+1 not in coins:
        answer = i+1
        break

print(answer)
