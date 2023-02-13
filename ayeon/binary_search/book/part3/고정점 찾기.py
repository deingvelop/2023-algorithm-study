import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

def fixed_point(arr):
    start = 0
    end = len(arr) -1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            start = mid +1
        else:
            end = mid -1
    return -1

print(fixed_point(arr))

