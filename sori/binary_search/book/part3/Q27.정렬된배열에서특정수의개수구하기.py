from bisect import bisect_left, bisect_right
n, x = map(int, input().split())

data = list(map(int, input().split()))

# 방법1 bisect 사용하기
left = bisect_left(data,x)
right = bisect_right(data,x)

print(left, right)
result = right - left 
print(result)