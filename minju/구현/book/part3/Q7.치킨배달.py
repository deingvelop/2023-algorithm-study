n, m = map(int, input().split())

maphome = []
mapchicken = []
for i in range(n) :
  x = list(map(int, input().split()))
  for j in range(len(x)):
    if x[j] == 1:
      maphome.append([i,j])
    elif x[j] == 2:
      mapchicken.append([i,j])
    else:
      continue

result = 99999
for chicken in combinations(mapchicken,m):
  temp = 0 #도시의 치킨거리
  for i in maphome:
    cd = [] #각 집마다 치킨거리 
    for j in range(m):
      d = abs(i[0]-chicken[j][0]) + abs(i[1]-chicken[j][1])
      cd.append(d)
    temp = temp + min(cd)
  result = min(result,temp)
  
print(result)
