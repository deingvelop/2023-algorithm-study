N = int(input())
arr = []

for _ in range(N):
    name, score = input().split()
    # print(name, score)
    score = int(score)
    arr.append([name, score])

arr.sort(key= lambda x:x[1])

for a in arr:
    print(a[0], end=' ')
