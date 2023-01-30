#두 배열의 원소 교체
#A의 합이 최대가 되도록
#A의 최솟값, B의 최댓값 변경 K번
#A의 원소의 합 최댓값 출력
n, k = map(int, input().split())

arrayA = list(map(int,input().split() ))
arrayB = list(map(int,input().split() ))

arrayA.sort()
arrayB.sort(reverse=True)
for i in range(k):
  if arrayB[i] > arrayA[i]:
    arrayA[i], arrayB[i] = arrayB[i], arrayA[i]
  else:
    break
      
result = 0
for i in arrayA:
  result += i

print(result)
print(sum(arrayA)) #for문 안돌려도됨..!