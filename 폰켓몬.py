def solution(a):
    b=list(set(a))
    if (len(a)//2)<len(b):
        return (len(a)//2)
    else:
        return len(b)