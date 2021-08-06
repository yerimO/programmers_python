def solution(n):
    aa=[]
    aaa=""
    while n>0:
        n,a=divmod(n,3)
        aa.append(a)
    for i in range(len(aa)):
        aaa+=str(aa[i])
    return int(aaa,3)