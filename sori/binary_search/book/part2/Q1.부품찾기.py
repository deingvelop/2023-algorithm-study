
n = int(input()) #가지고 있는 부품 개수
store = list(map(int, input().split() )) #가게에 있는 부품 리스트
m = int(input()) #요청하는 부품 개수
request = list(map(int, input().split() )) #요청하는 부품 리스트

#가게에 있는 부품 리스트 정렬
store.sort()

#가게 부품 리스트에 타겟이 있나 확인하는 함수
def binary_search(store, target, start, end):
  while start <= end:
    mid = (start + end) // 2 
    if store[mid] == target:
      return "yes"
    elif store[mid] > target: #중간점이 타겟 보다 클때 종료 지점을 중간-1로 변경
      end = mid - 1
    elif store[mid] < target:
      start = mid + 1
      
  return "no"

for i in request:
  print(binary_search(store, i, 0, n-1 ) ,end=" ")