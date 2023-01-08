# 문자열이 몇번 끊어졌는가!

# 0 1 0 1 0
# 5 덩어리 = 2
# 4 덩어리 = 2
# 3 덩어리 = 1
# 2 덩어리 = 1

arr = list(map(int, input()))

answer = 1  # 덩어리 수

for i in range(1,len(arr)):
    if arr[i] != arr[i-1]:
        answer +=1

answer //=2 # 몫

print(answer)
