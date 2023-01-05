#모험가 n명
#공포도 x인 모험가는 그룹인원이 x이상인 그룹에만 참여가능
#몇명은 남아도됨.
#그룹수의 최댓값 구하기
#최댓값중의 최솟값으로 묶기..

n = map(int, input().split())
data = list(map(int, input().split()))

data = data.sort()
result = 0
index = 0
for i in data.length():
  index += 1
  if data[i] >= index:
    result += 1
    index = 0

print(result)