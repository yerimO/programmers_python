def solution(price, money, count):
    answer = 0
    a=price
    for i in range(count):
        answer+=price
        price+=a
    if money>answer:
        return 0
    else:
        return answer-money
