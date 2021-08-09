def solution(n):
    li=set(range(2,n+1))
    for i in range(2,n+1):
        if i in li:
            li-=set(range(i*2,n+1,i))
    return len(li)