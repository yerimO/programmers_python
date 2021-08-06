def solution(arr):
    answer=[]
    answer.append(arr[0])
    arr.remove(arr[0])
    for i in arr:
        if answer and answer[-1]!=i :
            answer.append(i)

    return answer