def solution(s):
    answer = ''
    a=[]
    for i in range(len(s)):
        a.append(s[i])
    a=sorted(a,reverse=True)
    answer="".join(a)
    return answer