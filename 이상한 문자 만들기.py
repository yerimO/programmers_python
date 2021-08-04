def solution(s):
    answer = ''
    a=0
    for i in range(len(s)):
        if a%2==0:
            answer+=s[i].upper()
        else:
            answer+=s[i].lower()
        a+=1
        if s[i]==' ':
            a=0
    return answer