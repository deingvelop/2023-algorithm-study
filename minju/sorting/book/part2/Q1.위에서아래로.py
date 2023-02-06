n = int(input())

array = []
for i in range(n):
	array.append(int(input()))
    
array.sort(reverse=True) #역순 정렬

for i in array:
  print(i,end=' ')
