alphabet = [0]*26

S = input()

sum = 0

for s in S:
    if s.isdigit() == True :# 숫자 판별
        sum += int(s)
    else:
        alphabet[ord(s)-ord('A')] += 1

for idx, val in enumerate(alphabet):
    if val != 0:
        print(chr(idx +ord('A'))*val, end='')

print(sum)
