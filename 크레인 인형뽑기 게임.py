def solution(board, moves):
    new=[]
    cnt=0
    cnt1=0
    for i in moves:
        cnt=0
        for j in range(len(board)):
            if board[j][i-1]!=0 :
                new.append(board[j][i-1])
                if len(new)>=2 and (new[len(new)-1]==new[len(new)-2]):
                    new.pop()
                    new.pop()
                    cnt1+=2
                board[j][i-1]=0
                break

    return cnt1