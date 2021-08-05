def solution(N, stages):
    a=[]
    b=[]
    c=[]
    for i in range(N):
        cnt=[0,0]
        for j in stages:
            if (i+1)<j:
                cnt[1]+=1
            elif (i+1)==j:
                cnt[1]+=1
                cnt[0]+=1
        if cnt[1]==0:
            a.append(0)
        else:
            a.append(cnt[0]/cnt[1])
    b=sorted(a,reverse=True)
    
    for i in b:
        if i in a:
            c.append(a.index(i)+1)
            a[a.index(i)]=-1
    
    return c