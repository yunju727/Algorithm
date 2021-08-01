from sys import stdin

S = list(map(int, stdin.readline().split()))    # S[0] = 아이스크림 개수, S[1] = 먹을 수

I = list(map(int, stdin.readline().split()))    # 각 아이스크림 양

li = list()

for i in range(S[0]):
    li.append([i+1,I[i]])   # li[0] = [번호,양]

li = sorted(li, key= lambda x : (x[-1],x[0]))
li2 = list()

li2.append([[li[0][1]],li[0][0]])
t = li[0][1]    # 기준 양
ti = 0
for i in range(1,S[0]):
    if li[i][1] == t:
        li2[ti].append(li[i][0])    # 번호 추가
        t = li[i][1]
    else:
        ti+=1
        li2.append([[li[i][1]],li[i][0]])
        t = li[i][1]

ch = False

idn = len(li2)-1    # 뒤에서부터 진행하기 위한 인덱스
while S[1]>0:
    if(ch): # 민트초코를 먹어 뒤집어서 진행하는 경우
        if len(li2[idn])>1: # 해당 배열에 값이 남아있는 경우
            num = li2[idn][0][0]    # 아이스크림 번호
            amount = li2[idn][-1]
            print(amount)
            del li2[idn][-1]
        else:
            idn-=1
            num = li2[idn][0][0]
            amount = li2[idn][-1]
            print(amount)
            del li2[idn][-1]
        if num % 7 == 0:  # 민트초코
            ch = not ch
    else:
        if len(li2[idn])>1:
            num = li2[idn][0][0]
            amount = li2[idn][1]
            print(amount)
            del li2[idn][1]
        else:
            idn-=1
            num = li2[idn][0][0]
            amount = li2[idn][1]
            print(li2[idn][1])
            del li2[idn][1]
        if num % 7 == 0:    # 민트초코
            ch = not ch
    S[1]-=1
