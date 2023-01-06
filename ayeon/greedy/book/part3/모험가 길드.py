N = int(input())
arr = list(map(int,input().split()))

arr.sort(reverse=True) # 정렬

i=0
answer =0

while i<len(arr):
    i +=+arr[i] # arr[i:i+arr[i]] 가 한 묶음
    if (i<=len(arr)):   # i+arr[i] 가 len(arr-1) 작을 때, 그룹 생성
        answer +=1

print(answer)
