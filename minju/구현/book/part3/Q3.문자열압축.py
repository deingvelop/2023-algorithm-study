"""참고한 사이트> https://eunhee-programming.tistory.com/135"""

def solution(s):
    result=[] #쪼갠 문자열의 길이들을 담는 list
    
    if len(s)==1:
        return 1 #문자열s가 1일 때 반환 값은 항상 1
      
    for i in range(1, (len(s)//2)+1):  #문자열을 쪼갤 수 있는 최대 길이는 문자열s의 반
        b = '' #매번 쪼갰을 때 나오는 문자열 저장 
        cnt = 1 #문자열이 연속으로 반족되는지 체크하는 변수 
        
        tmp=s[:i] #그 다음 문자열과 연속되는지 비교하기 위한 변수, 문자열을 쪼갤 때 처음 부분은 무조건 tmp에 넣어줌

        for j in range(i, len(s), i): #i길이만큼 문자열을 쪼갬
            if tmp==s[j:i+j]: #비교하기 위한 문자 tmp와 새로 쪼갠 문자가 같으면 cnt +1
                cnt+=1
            else:
                if cnt!=1: #tmp와 다른데 cnt가 1이 아니면 
                    b = b + str(cnt)+tmp #b에 cnt(갯수)와 반복문자열 넣어줌
                else: #cnt가 1이면 
                    b = b + tmp  #그냥 b뒤에 바로 tmp 붙여줌
                tmp=s[j:j+i] #새로운 tmp 생성하고
                cnt = 1 #cnt는 1로 리셋 
                
        if cnt!=1: #마지막 tmp에 담은 문자를 b변수에 추가하기 위함 
            b = b + str(cnt) + tmp
        else:
            b = b + tmp
                
        result.append(len(b)) #문자열 길이 구해서 result배열에 추가
        
    return min(result) #길이 중 최소값 리턴 
