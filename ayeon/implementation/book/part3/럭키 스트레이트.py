#1
N = input()

answer = 0

length = len(N)//2

for i in range(length):
    answer += int(N[i])

for i in range(length):
    answer -= int(N[len(N)-1-i])

if answer == 0:
    print("LUCKY")
else:
    print("READY")

#2
N = list(map(int,input()))

if sum(N[0:len(N)//2]) == sum(N[len(N)//2:]):
    print("LUCKY")
else:
    print("READY")
