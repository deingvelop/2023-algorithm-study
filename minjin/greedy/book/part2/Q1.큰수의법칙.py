n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
answer = 0

max_num = max(numbers)
numbers.remove(max_num)
second_max_num = max(numbers)

for _ in range(m):
    if cnt < k:
        answer += max_num
        cnt += 1
    else:
        answer += second_max_num
        cnt = 0

print(answer)