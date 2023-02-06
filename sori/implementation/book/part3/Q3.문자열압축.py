data = input()
c = 0
min_len= int(len(data))


for step in range(1,len(data)//2+1):
  result = ''
  pre = data[0:step]
  count = 1
  for j in range(step,len(data),step):
      now = data[j:j+step]
      if(pre == now):
        count += 1
      else:
        if(count >= 2):
           result += str(count)+pre
        else:
          result += pre
        count = 1
      pre = now 

  if(count >= 2):
    result += str(count)+pre
  else:
    result += pre
  

  min_len = min(min_len, len(result))

print(min_len)

#어떻게 구현할지 생각은 대충 났는데 그걸 코드로 표현하기가 어려웠다.
#이중 포문으로 해야 하는 것은 생각했는데 문자열 자를때 전체 문자열의 반까지만 잘라야 하는걸 나중에 생각났다
