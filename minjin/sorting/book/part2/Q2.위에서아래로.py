n = int(input())
answer = []

for _ in range(n):
    answer.append(int(input()))

answer.sort()
answer.reverse()
print(*answer)