def solution(s):
    cnt=0
    num=['1','2','3','4','5','6','7','8','9','0']
    for i in s:
        for j in num:
            if i==j:
                cnt+=1
    if cnt==len(s) and (len(s)==4 or len(s)==6):
        return True
    else:
        return False
    