def solution(a):
    an=[]
    for i in range(0,len(a),1):
        cnt=0
        for j in range(i+1,len(a),1):
            cnt+=1
            if a[i]>a[j]:
                break
        an.append(cnt)
    return an