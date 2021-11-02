def solution(s, n):
    answer=''
    for i in s:
    #여백은 여백으로 반환
        if i==' ':
            answer+=i

        # 대문자인지 소문자인지 판별

        # 소문자
        if i.islower():
            if ord(i)+n<123 :
                answer+=chr(ord(i)+n)
            else:
                answer+=chr(ord(i)-26+n)

        # 대문자
        elif i.isupper() :
            if ord(i)+n<91:
                answer+=chr(ord(i)+n)
            else:
                answer+=chr(ord(i)-26+n)
    return answer