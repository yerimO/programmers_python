def solution(dart):
    num=[]
    STD=['S','D','T']
    sum=0
    for i in range(len(dart)):
        
        if dart[i] in STD and dart[i-1]!='0':
            num.append(int(dart[i-1])**(STD.index(dart[i])+1))
        
        elif dart[i]=='0':
            if dart[i-1]=='1':
                num.append(10**(STD.index(dart[i+1])+1))
            else:
                num.append(0**(STD.index(dart[i+1])+1))

        elif dart[i]=='*':
            if len(num)==1:
                num[len(num)-1]=num[len(num)-1]*2
            else:
                num[len(num)-1]=num[len(num)-1]*2
                num[len(num)-2]=num[len(num)-2]*2

        elif dart[i]=='#':
            num[len(num)-1]=((num[len(num)-1])*-1)

    for i in num:
        sum+=i

    return sum