data = list(input())
toZero = 0
toOne = 0
print(data)
if data[0] == '0':
    toOne += 1 
else:
    toZero += 1

for i in range(len(data)-1):
  if data[i] != data[i+1]:
      if data[i+1] == '0':
          toOne += 1 
      else :
          toZero += 1


print(f"toZero: {toZero}, toOne: {toOne}")
print(min(toZero, toOne))