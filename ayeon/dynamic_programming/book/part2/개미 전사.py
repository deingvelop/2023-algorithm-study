N = int(input())
arr = list(map(int, input().split()))

d = [0] *N

d[0] = arr[0]
d[1] = max(d[0], d[1])

for i in range(2, N):
    d[i] = max(d[i-2]+arr[i], d[i-1])

print(d[-1])
