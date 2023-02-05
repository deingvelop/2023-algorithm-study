# 내 풀이
import sys
input = sys.stdin.readline


n = int(input())
goods = list(map(int, input().split()))
m = int(input())
required = list(map(int, input().split()))


def binary_search(arr, target):
    start = 0
    end = len(arr) -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return target
        elif target < arr[mid]:
            end = mid -1
        else:
            start = mid + 1
    return -1


answers = []
for r in required:
    result = binary_search(goods, r)
    if result != -1:
        answers.append("yes")
    else:
        answers.append("no")

print(*answers)


# 교재의 다른 풀이 1 - 계수 정렬
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")


# 교재의 다른 풀이 2 - 집합 set 자료옇 이용
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print("yes", end=" ")
    else:
        print("no", end=" ")