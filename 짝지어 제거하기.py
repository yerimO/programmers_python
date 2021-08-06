def solution(s):
    a=[]
    for i in s:
        if len(a)!=0 and a[-1]==i:
            del a[-1]
        else:
            a.append(i)
            
    if len(a)==0:
        return 0
    else:
        return 1