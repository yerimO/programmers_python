def solution(lottos, win_nums):
    cnt=[0,0]
    for i in lottos:
        if i in win_nums:
            cnt[1]+=1
            cnt[0]+=1
        if i==0:
            cnt[0]+=1
    if cnt[1]==0 and cnt[0]==6:
        cnt[0]=7-cnt[0]
        cnt[1]=7-cnt[0]
    elif cnt[0]==0 and cnt[1]==0:
        cnt[0]=6
        cnt[1]=6
    elif cnt[1]==0 and cnt[0]<6:
        cnt[0]=7-cnt[0]
        cnt[1]=6
    elif cnt[1]==1:
        cnt[0]=7-cnt[0]
        cnt[1]=6
    elif cnt[1]!=1 and cnt[0]!=1:
        cnt[0]=7-cnt[0]
        cnt[1]=7-cnt[1]
    return cnt