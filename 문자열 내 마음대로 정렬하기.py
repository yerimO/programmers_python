def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        answer.append(strings[i][n]+strings[i])
        
    answer.sort()
    
    for i in range(len(strings)):
        answer[i]=answer[i][1:]
    return answer