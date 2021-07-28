def solution(n):
    list=[]
    n=str(n)
    
    for i in n:
        list.append(int(i))
    #내림차순    
    list=sorted(list,reverse=True)
    n=''
    for i in list:
        n+=str(i)
    n=int(n)
    #return int("".join(sorted(list(str(n)),reverse=True)))
    return n