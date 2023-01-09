n = int(input())
times = list(map(int, input().split()))
answer = 0

times.sort()
for i in range(len(times)):
    answer += sum(times[:i+1])

print(answer)