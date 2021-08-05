def solution(a, b):
    answer = 0
    num=[a,b]
    for i in range(min(num),max(num)+1,1):
        answer+=i
    return answer