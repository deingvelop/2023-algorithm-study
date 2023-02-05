# 풀이 1 - 시간복잡도 고려 X
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
numbers = list(map(int, input().split()))
print(numbers.count(x))


# 풀이 2 - 이진탐색
import sys

input = sys.stdin.readline

n, x = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid
    return False


mid_x = binary_search(numbers, x)
if mid_x == False:
    print(-1)
else:
    first_x = binary_search(numbers[:mid_x], x)
    last_x = binary_search(numbers[mid_x+1:], x) + mid_x + 1
    first, last = False, False

    while True:
        if numbers[first_x] == x and (numbers[first_x - 1] != x or first_x == 0):
            first = True
        else:
            first_x = binary_search(numbers[first_x + 1:], x)
            if not first_x:
                first_x = mid_x
                first = True
        if numbers[last_x] == x and (numbers[last_x + 1] != x or last_x == len(numbers) - 1):
            last = True
        else:
            last_x = binary_search(numbers[:last_x], x)
            if not last_x:
                last_x = mid_x
                last = True
            last_x += mid_x + 1
        if first == last == True:
            break

    print(last_x - first_x + 1)


# 모범 답안 - 교재 풀이 1
def count_by_value(array, x):
    n = len(array)

    a = first(array, x, 0, n - 1)
    if a == None:
        return 0

    b = last(array, x, 0, n - 1)

    return b - a + 1


# 처음 위치를 찾는 이진 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)


# 마지막 위치를 찾는 이진 탐색 메서드
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)


n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)
if count == 0:
    print(-1)
else:
    print(count)


# 모범 답안 - 교재 풀이 2
# bisect : 파이썬의 이진 탐색 라이브러리
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 [x, x]인 데이터의 개수를 반환하는 함수
count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)