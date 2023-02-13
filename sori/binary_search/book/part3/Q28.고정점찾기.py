#고정 점 찾기
n = int(input())
arr = list(map(int, input().split()))

def find(array, start, end):
  if start > end:
    return None
  mid = (start+end)//2
  if array[mid] == mid:
    return mid
  elif array[mid] < mid:
    return find(array, mid+1, end)
  elif array[mid] > mid:
    return find(array, start, mid-1)

result = find(arr,0,n-1)
if result == None:
  print(-1)
else:
  print(result)