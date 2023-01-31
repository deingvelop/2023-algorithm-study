import sys
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int, input().split()))

M = int(input())
arr2 = list(map(int, input().split())) 

def binary_search(arr, target, start, end):
    while start<= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return None

arr1.sort()
for a in arr2:
    if binary_search(arr1, a, 0, N-1) != None:
        print("yes", end=' ')
    else:
        print("no", end =' ')

# < 집합 >
# 시간 복잡도 O(M*N)

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
