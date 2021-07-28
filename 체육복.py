# def solution(n, lost, reserve):
#     answer = 0
#     cnt=0
        
#     for i in lost:
#         if i+1 in reserve :
#             reserve.remove(i+1)
#             lost.remove(i)
#         elif i-1 in reserve:
#             reserve.remove(i-1)
#             lost.remove(i)
#         else:
#             cnt+=1
   
#     answer=n-cnt
#     return answer

n=5
lost=[2,4]
reserve=[1,3,5]

#여벌 체육복 학생 도난 중복 제거
for i in lost: 
    if i in reserve:
        lost.remove(i)
        reserve.remove(i) 
# print(lost)
# print(reserve)
for j in reserve:
    for i in lost:
        if i==j-1 :
            lost.remove(i)
            reserve.remove(j)        
            print(lost)
            print(reserve)
        if i==j+1:
            lost.remove(i)
            reserve.remove(j)        
            print(lost)
            print(reserve)
print(n-len(lost))  