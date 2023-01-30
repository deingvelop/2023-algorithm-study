n = int(input())
scores = []

for _ in range(n):
    student, k, y, s = input().split()
    scores.append((student, int(k), int(s), int(y)))

scores.sort(key=lambda x : (-x[1], x[3], -x[2], x[0]))

for s in scores:
    print(s[0])