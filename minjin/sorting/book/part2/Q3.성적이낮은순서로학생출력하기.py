n = int(input())
data = []

for _ in range(n):
    student, score = input().split()
    data.append((student, int(score)))

data.sort(key=lambda x: x[1])

answer = []
for d in data:
    answer.append(d[0])

print(*answer)