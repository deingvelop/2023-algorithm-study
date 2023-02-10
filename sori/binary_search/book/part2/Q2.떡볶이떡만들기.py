#내풀이
#떡볶이 떡이 딱 맞아 떨어지지 않을수도 있음..

n, m = map(int, input().split())
data = list(map(int, input().split()))

#리스트에 있는 값을 정렬한 후 중간 값부터 잘라본다.
#만족하나? -> 그것보다 큰값으로 잘라보기
#불만족하나? - >그것보다 작은 값으로 잘라보기
#딱 맞나? - > 절단기 값

data.sort()

def binary_search(data, start, end, m):
  if start > end:
    return -1
  mid = (start + end) // 2
  cut = data[mid] #절단 높이
  result = 0 #남은 떡 합친 길이
  
  for i in data: # 리스트에 담긴 떡 다 잘라보기
    lest = i - cut
    if lest > 0: #자르고 남은게 0보다 클때 더하기
      result += lest

  if result == m: #남은 값이 원하는 값이랑 같으면
    return cut
  elif result > m: #남은 값이 원하는 값보다 크면 더 크게 잘라보기
    return binary_search(data, mid+1, end, m)
  elif result < m: #남은 값이 원하는 값보다 작으면 더 작게 잘라보기
    return binary_search(data, start, mid-1, m)


print(binary_search(data, 0, len(data)-1 , m))


#고친 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
start = 0
end = max(data)
result = 0
while start < end:
    cut = (start + end) // 2 #절단 높이 중간값
    sumVal = 0 #남은 떡 합친 길이
  
    for i in data: # 리스트에 담긴 떡 다 잘라보기
      lest = i - cut
      if lest > 0: #자르고 남은게 0보다 클때 더하기
        sumVal += lest
  
    if sumVal >= m: #남은 값이 원하는 값보다 크면 기록하고 더 크게 잘라보기
      result = cut
      start = cut + 1
    elif sumVal < m: #남은 값이 원하는 값보다 작으면 더 작게 잘라보기
      end = cut -1 

print(result)