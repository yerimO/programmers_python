def solution(n):
    a=n**0.5
    if int(a)**2==n:
        return (int(a)+1)**2
    else:
        return -1
