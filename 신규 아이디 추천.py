id='.........b'
new_id=''
ok=['1','2','3','4','5','6','7','8','9','0','-','_','.']

# 맨 앞 맨 뒤 . 제거
def remove_del(new_id):
    if new_id[0]=='.' :
        new_id =new_id[1:]
        if len(new_id)==0:
            return new_id
    if new_id[len(new_id)-1]=='.':
        new_id =new_id[:len(new_id)-1]
        if len(new_id)==0:
            return new_id
    return new_id

# 빈 문자열 처리
def plus(new_id):
    new_id+='a'
    return new_id

#처음에 빈 문자열인지 확인
if len(id)==0:
    plus(new_id)

# 아이디 규칙 확인 절차
for i in id:

    #대문자 소문자로 변환 후 new_id에 포함한다.
    if 65<=ord(i)<=90:
        new_id+=i.lower()

    #소문자와 허용 문자는 포함한다
    elif i in ok or 97<=ord(i)<=122:

        # . 중복 삭제
        if i=='.' and len(new_id)!=0:
            if new_id[len(new_id)-1]!='.':
                new_id+=i
        else:
            new_id+=i

new_id=remove_del(new_id)

# new_id 가 15자 이상이면 15자까지 허용
if len(new_id)>15:
    new_id=new_id[0:15]
    new_id=remove_del(new_id)

#new_id 길이가 0일 때
elif len(new_id)==0:
    new_id='aaa'
#2글자 이하일 때 실행 명령어
elif len(new_id)<3:
    while True:
        new_id+=new_id[len(new_id)-1]
        if len(new_id)==3:
            break


print(new_id)

