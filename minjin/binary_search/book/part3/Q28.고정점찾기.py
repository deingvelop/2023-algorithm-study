import sys
input = sys.stdin.readline


def find_fixed_point(array, target):
    start = 0
    end = len(array)
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < mid:
            start = mid + 1
        elif arr[mid] > mid:
            end = mid - 1
        else:
            return mid
    return -1


n = int(input())
arr = list(map(int, input().split()))
print(find_fixed_point(arr, n))