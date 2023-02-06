data = input()
number = 0
al = []
for i in range(len(data)) :
  print(int(ord(data[i])))
  if(65 <= int(ord(data[i])) <= 90 ) :
    al.append(data[i])
  else :
    number += int(data[i])

al.sort()
al.append(str(number))

print(''.join(al))