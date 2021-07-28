def ss(i,j,k):
    cnt=0
    num=i+j+k
    for i in range(2,num+1,1):
        if num%i==0:
            cnt+=1
        if cnt>=2:
            break
        
    if cnt==1:
        return 1
    else:
        return 0

def solution(nums):
    cnt=0
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if ss(nums[i],nums[j],nums[k])==1:
                    cnt+=1
    return cnt