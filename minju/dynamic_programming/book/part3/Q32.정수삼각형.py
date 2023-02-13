n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
for i in range(1, len(array)):
    for j in range(i+1):
        if j == 0: #원소가 왼쪽 끝에 있는 경우
            array[i][j] = array[i][j] + array[i-1][j]
        elif i == j: #원소가 오른쪽 끝에 있는 경우
            array[i][j] = array[i][j] + array[i-1][j-1]
        else: #원소가 그 외에 있는 경우 
            array[i][j] = array[i][j] + max(array[i-1][j], array[i-1][j-1])

print(max(array[-1]))
