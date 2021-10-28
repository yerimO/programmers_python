def solution(s):
    new_s=''
    answer=''
    number=['0','1','2','3','4','5','6','7','8','9']
    s_number=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in s:
        if i in number:
            answer+=i
        else:
            new_s+=i
            if new_s in s_number:
                answer+=str(s_number.index(new_s))
                new_s=''
    return int(answer)