S = input()

ss = list(S)
ss.sort()

sum=0
idx = 0
for i in range(len(ss)):
  if ord(ss[i])>= 48 and ord(ss[i])<= 57:
    sum = sum + int(ss[i])
  else:
    idx = i
    break
    
print((''.join(ss[idx:]))+str(sum))   
