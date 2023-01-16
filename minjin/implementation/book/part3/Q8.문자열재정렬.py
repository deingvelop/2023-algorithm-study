s = list(input())
chars = []
numbers = []

for i in range(len(s)):
    if '0' <= s[i] <= '9':
        numbers.append(s[i])
    else:
        chars.append(s[i])

chars.sort()
numbers = list(map(int, numbers))

print(''.join(chars) + str(sum(numbers)))