import random

# n 이 판의 총 병사 수 (범위 50~100)
# game 전체 게임에서 이 게임이 몇번째 게임인지 알려줌
# myn 내가 현재 가지고 있는 총 병사 수
# m 이 판에서 진행될 총 턴 수 (범위 3~n/5)
# oparr 상대가 여태껏 낸 병사 수가 저장된 배열
# return 값이 자기가 가지고 있는 병사보다 클 시 모든 병사를 내보내는 것으로 처리
# 여러분이 짠 코드를 strategy 함수에 넣어서 테스트 해 보세요

arr1=[[0]*100 for _ in range(100)]
arr2=[[0]*100 for _ in range(100)]
n,m=0,0
n_a=0,0
n_b=0,0
w_a,w_b=0,0

#평균 값을 return하는 전략. 가장 쉽게 생각할 수 있는 전략
def s1(game,turn,myn,oparr):
    if turn==m-1:
        return myn
    return n//m

#위의 전략을 저격하여 만든 전략. 1턴에만 져주고, 나머지 턴을 비김 or 승리함
def s2(game,turn,myn,oparr):
    if turn==0:
        return 0
    elif turn==m-1:
        return myn
    else:
        return n//(m-1)

#상대방이 전 턴에 낸 병사 수만큼 내는 전략
def s3(game,turn, myn, oparr):
    if turn==0:
        return 0
    elif turn==m-1:
        return myn
    else:
        return oparr[game][turn-1]
    
#여러분의 아이디어를 펼쳐 보세요
def strategy(game,turn, myn, oparr):
    return 0

for i in range(10):
    n=n_a=n_b=random.randint(50,100)
    m=random.randint(3,n//5)
    s_a,s_b=0,0
    for j in range(m):
        n1=s1(i,j,n_a,arr2) #s1을 s2, s3로 바꿔 테스트 해 보세요
        n2=strategy(i,j,n_b,arr1) 
        if n1>n_a:
            n1=n_a
        if n2>n_b:
            n2=n_b
        arr1[i][j]=n1
        arr2[i][j]=n2
        n_a-=n1
        n_b-=n2
        if n1>n2:
            s_a+=1
        elif n1<n2:
            s_b+=1
    print("turn "+str(i+1)+" : \n");
    print(arr1[i][:m])
    print(arr2[i][:m])
    if s_a>s_b:
        w_a+=1
        print("a win")
    elif s_a<s_b:
        w_b+=1
        print("b win")
    else:
        print("draw")


print()
print()
if w_a>w_b:
    print("p1 win!")
elif w_a<w_b:
    print("p2 win!")
    
