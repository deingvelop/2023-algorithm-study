import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()

start = 0
end = len(heights) -1

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in range(mid+1, len(heights)):
        sum += heights[i] - heights[mid]
    if sum >= m:
        print(heights[mid])
        break