def ss(i):
    cnt=0
    for j in range(1,i+1,1):
        if i%j==0:
            cnt+=1
    if cnt%2==0:
        return 0
    else:
        return 1

def solution(left, right):
    answer = 0
    for i in range(left,right+1,1):
        if ss(i)==0:
            answer+=i
        else:
            answer-=i
    return answer