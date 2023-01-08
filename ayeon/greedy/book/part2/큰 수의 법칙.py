N, M, K = map(int, input().split())
arr = list(map(int, input().split())

arr.sort(reverse=True) # 정렬

answer = 0
while(M>=K):
	answer += arr[0]*K
	M-=K
  answer += arr[1]
	M-=1

answer += arr[0]*M
print(answer)
