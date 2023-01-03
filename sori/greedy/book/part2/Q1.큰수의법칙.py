#N(배열의 크기), M(숫자 더해지는 횟수) , K(연속으로 더할수 있는 횟수) 자연수 받기 (공백으로 구분)
#print("숫자입력 :  ",end='')
n, m, k = map(int , input().split())

#N개의 자연수(1~10000) 중복 허용 (공백으로 구분) 
data = list(map(int, input().split()))

#K <= M 

#해결법: 가장 큰 수를 K번 더하고 두 번째로 큰 수를 1번 더하기 반복.. M번까지
data.sort()

max = data[n-1]
max_minus_one = data[n-2]

#print("max :", max, "max-1 :",max_minus_one)
result = 0
count = 0

while (count <= m):
    for _ in range(k):
      if count == m : 
          break
      else:
          result += max
          count += 1
          #print(max, end='+')
    if count == m : 
          break
    else:    
        result += max_minus_one
        count += 1
        #print(max_minus_one, end='+')

#print()
print(result)