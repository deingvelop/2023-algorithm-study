num_list = list(map(int, list(input())))

mid = len(num_list) // 2
sum1, sum2 = 0, 0

for i in range(mid):
    sum1 += num_list[i]
    sum2 += num_list[mid + i]

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")