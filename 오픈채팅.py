def solution(record):
    an={}
    ans=[]
    for i in record:
        li=i.split(" ")
        if li[0]=="Enter":
            an[li[1]]=li[2]
        elif li[0]=="Change":
            an[li[1]]=li[2]


    for i in record:
        li=i.split(" ")
        if li[0]=="Enter":
            ans.append(an[li[1]]+"님이 들어왔습니다.")
        elif li[0]=="Leave":
            ans.append(an[li[1]]+"님이 나갔습니다.")

    return ans