N, K = map(int, input().split())

answer = 0

while(N>1):
	mod = N%K
	if mod == 0:
		answer +=1
		N/=K
	else:
		N -= mod
		answer += mod
	
print(answer)
