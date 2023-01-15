input_data = int(input())
data = list(map(int, str(input_data)))

if sum(data[:len(data)//2]) == sum(data[len(data)//2:]):
  print('LUCKY')
else:
  print('READY')
