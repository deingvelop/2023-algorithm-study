data = list(input())
intData = list(map(int,data))
a = 0
b = 0
for i in range(len(intData)):
  if i < len(intData)/2:
    a += intData[i]
  else:
    b += intData[i]

if(a == b):
  print('LUCKY')
else:
  print('READY')