def solution(n):
    answer = []
    n=str(n)

    for i in range(0,len(n),1):
        answer.append(int(n[len(n)-(i+1)]))
    return answer