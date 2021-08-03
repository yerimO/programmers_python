def solution(s):
    cnt=[0,0]
    for i in s:
        if i == 'p' or i=='P':
            cnt[0]+=1
        elif i=='y'or i=='Y':
            cnt[1]+=1
    if cnt[0]==cnt[1] or (cnt[0]==0 and cnt[1]==0):
        return True
    else:
        return False
