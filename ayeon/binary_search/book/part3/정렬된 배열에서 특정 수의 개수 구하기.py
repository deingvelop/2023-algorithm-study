import sys
input = sys.stdin.readline

N, x = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = N-1

def binary_search(arr, target, start, end):

    while start <= end:
        mid = (start+end) // 2

        if arr[mid] == target:
            return binary_search(arr, target, start, mid-1)
            + binary_search(arr, target, mid+1, end) + 1

        elif arr[mid] < target:
            start = mid +1
        
        else:
            end = mid -1
    return 0

answer = binary_search(arr, x, 0, N-1)
if answer ==  0:
    print(-1)
else:
    print(answer)
