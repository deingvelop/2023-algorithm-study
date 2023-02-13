n, c = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()

start = 1    #최소 거리
end = array[-1] - array[0]   #최대 거리
answer = 0

binary_search(array, start, end)
print(answer)


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2   #기준이 되는 사이 거리
        current = array[0]
        count = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:    #좌표가 기준 거리 이상에 위치하는 경우
                count += 1       #개수를 셈
                current = array[i]

        if count >= c:
            global answer
            start = mid + 1   #사이 거리 넓히기 
            answer = mid
        else:
            end = mid - 1     #사이 거리 좁히기
