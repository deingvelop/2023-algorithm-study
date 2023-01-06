data = list(input())
print(data)
data = list(map(int, data))
print(data)
result = data[0]


for i in range(len(data)-1):
  print(result, data[i+1])
  if result ==0 or data[i+1] ==0:
    result += data[i+1]
  else:
    result *= data[i+1]

print(result)