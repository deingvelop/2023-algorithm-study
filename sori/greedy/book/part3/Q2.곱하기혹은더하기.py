data = list(input())
print(data)
data = list(map(int, data))
print(data)
result = data[0]


for i in range(len(data)-1):
  print(result, data[i+1])
  if result <=1 or data[i+1] <= 1:
    result += data[i+1]
  else:
    result *= data[i+1]

print(result)