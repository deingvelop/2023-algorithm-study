from bisect import bisect_left, bisect_right
n, x = map(int, input().split())

data = list(map(int, input().split()))

# 방법1 bisect 사용하기
left = bisect_left(data,x)
right = bisect_right(data,x)

result = right - left 
print(result)


# 방법2 이진트리로 가장 첫번재 인덱스와 마지막 인덱스를 찾아서 빼줌
def find_first(data, start, end, target):
  if start > end:
    return 0
  mid = (start+end)//2
  #해당 값을 가지는 원소 중에서 가장 왼쪽(또는 0)에 있는 경우에만 인덱스 반환
  if(mid == 0 or data[mid-1] < target ) and data[mid] == target:
    return mid
  #중간점의 값보다 찾는 값이 작거나 같은 경우 왼쪽 확인
  elif data[mid] >= target:
    return find_first(data, start, mid-1, target)
  #중간점의 값보다 찾는 값이 큰 경우 오른쪽 확인
  else:
    return find_first(data, mid+1, end, target)
  
def find_last(data, start, end, target):
  if start > end:
    return 0
  mid = (start+end)//2
  #해당 값을 가지는 원소중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
  if(mid == n-1 or data[mid+1] > target ) and data[mid] == target:
    return mid
  #중간점의 값 보다 찾는 값이 작은 경우 왼쪽 확인
  elif data[mid] > target:
    return find_last(data, start, mid-1, target)
  #중간점의 값보다 찾는 값이 크거나 같은 경우 오른쪽 확인
  else:
    return find_last(data, mid+1, end, target)
      
last = find_last(data, 0, n-1, x)
first = find_first(data,0, n-1, x)
if last != 0:
  #마지막으로 등장한 인덱스 - 처음 등장한 인덱스 + 1
  print(last - first +1)
else:
  print(-1)