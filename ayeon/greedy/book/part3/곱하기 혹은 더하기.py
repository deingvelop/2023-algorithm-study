# if answer==0:
#     answer += arr[i]
# else:
#     answer *= arr[i]

# input : 012012
# output : 8 > 4

arr = list(map(int, input()))

answer = 0
idx =0

if arr[0] == 0: # 1번째가 0인 경우
    for i in range(1, len(arr)):
        if arr[i]==0:
            i+=1
            continue
        if answer==0 or answer+arr[i]>answer*arr[i]:
            answer += arr[i]
        else:
            answer *= arr[i]
else:
    for i in range(0, len(arr)):
        if arr[i]==0:
            i+=1
            continue
        if answer==0 or answer+arr[i]>answer*arr[i]:
            answer += arr[i]
        else:
            answer *= arr[i]

print(answer) 
