def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if (numbers[i]+numbers[j]) not in answer and (numbers[i]!=numbers[j]):
                answer.append(numbers[i]+numbers[j])
            if (numbers[i]+numbers[j]) not in answer and (numbers[i]==numbers[j]) :
                if numbers.count(numbers[i])>=2:
                    answer.append(numbers[i]+numbers[j])

    answer.sort()
    return answer