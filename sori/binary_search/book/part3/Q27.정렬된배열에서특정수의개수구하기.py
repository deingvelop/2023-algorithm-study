from bisect import bisect_left, bisect_right
n, x = map(int, input().split())

data = list(map(int, input().split()))

# 방법1 bisect 사용하기
left = bisect_left(data,x)
right = bisect_right(data,x)

print(left, right)
result = right - left 
print(result)


# 방법2 이진트리로 가장 첫번재 인덱스와 마지막 인덱스를 찾아서 빼줌
def find_first(data, start, end, target):
  if start > end:
    return 0
  mid = (start+end)//2
  if(mid == 0 or data[mid-1] < target ) and data[mid] == target:
    return mid
  elif data[mid] >= target:
    return find_first(data, start, mid-1, target)
  else:
    return find_first(data, mid+1, end, target)
  
def find_last(data, start, end, target):
  if start > end:
    return 0
  mid = (start+end)//2
  if(mid == n-1 or data[mid+1] > target ) and data[mid] == target:
    return mid
  elif data[mid] > target:
    return find_last(data, start, mid-1, target)
  else:
    return find_last(data, mid+1, end, target)
      
print(find_last(data, 0, n-1, x) , find_first(data,0, n-1, x))
print(find_last(data, 0, n-1, x) - find_first(data,0, n-1, x)+1)