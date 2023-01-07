S = list(map(int, input()))

sum = S[0]

for i in S[1:]:
  if sum == 0:
    sum = sum + i
  else:
    if i == 0:
      sum = sum + i
    else:
      sum = sum * i
  
print(sum)
