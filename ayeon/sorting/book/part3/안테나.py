import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

if N %2 == 0:
    mid = N//2 -1
else:
    mid = N//2
    
print(arr[mid])
