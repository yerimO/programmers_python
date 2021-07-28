def solution(n, lost, reserve):
    
    #여벌 체육복 학생 도난 중복 제거
    yeppi=set(reserve)-set(lost)
    yerim=set(lost)-set(reserve)

            
    for j in yeppi:
        if j-1 in yerim:
            yerim.remove(j-1)
        elif j+1 in yerim:
            yerim.remove(j+1)
            
    return n-len(yerim)