def solution(answers):
    yerim=answers
    a=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    cnt=[0,0,0]

    #정답 개수만큼 cnt증가
    for i in range(len(yerim)):
        if yerim[i]==a[0][i%5]:
            cnt[0]+=1
        if yerim[i]==a[1][i%8]:
            cnt[1]+=1
        if yerim[i]==a[2][i%10]:
            cnt[2]+=1

    #중복 제거 및 인덱스 출력
    b=max(cnt)
    y=[]
    for i in range(len(a)):
        if b==cnt[i]:
            y.append(i+1)

    return list(set(y))