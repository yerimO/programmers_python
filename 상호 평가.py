def solution(sc):
    ans=""
    for i in range(len(sc)):
        l=len(sc)
        an=[]
        sum=0
        for j in range(len(sc)):
            an.append(sc[j][i])
        if (max(an)==sc[i][i]) or (min(an)==sc[i][i]):
            if an.count(sc[i][i])==1:
                an.remove(sc[i][i])
                l-=1
        for k in an:
            sum+=k

        if sum/l>=90:
            ans+='A'
        elif 90>sum/l>=80:
            ans+='B'
        elif 80>sum/l>=70:
            ans+='C'
        elif 70>sum/l>=50:
            ans+='D'
        else:
            ans+='F'
    return ans