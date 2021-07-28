def solution(x):
    answer=0
    x=str(x)
    for i in x:
        answer+=int(i)
    if int(x)%answer==0:
        return True
    else:
        return False
