def solution(a, b):
    num=0
    day=['FRI','SAT','SUN','MON','TUE','WED','THU']
    mon=[31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(a-1):
        num+=mon[i]
    num+=b
    
        
    
    return  day[num%7-1]