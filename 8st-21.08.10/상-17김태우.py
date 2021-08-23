from sys import stdin

N = int(input())    # 돌의 개수

en = dict() # 점프 에너지

for i in range(1, N):
    en[i] = list(map(int, stdin.readline().split()))
K = int(input())

sm = [0,[[0,0],[0,0]]]  # 해당 번호까지 가는데 필요한 에너지의 리스트

for n in range(2, N+1):
    tmp = list()    # 임시 리스트 초기화
    tmp2 = list()
    if n == 2:
        tmp.append([sm[n - 1][0][0] + en[n - 1][0], 0])
        sm.append([tmp[0], tmp[0]])
    else:
        tmp.append([sm[n - 1][0][0] + en[n - 1][0], 0])
        tmp.append([sm[n - 2][0][0] + en[n - 2][1], 0])
        tmp = sorted(tmp, key=lambda x: x[0])
        if n >= 4:  # 매우 큰 점프 가능
            tmp2.append([sm[n - 1][1][0] + en[n - 1][0], 1])
            tmp2.append([sm[n - 2][1][0] + en[n - 2][1], 1])
            tmp2.append([sm[n-3][0][0]+K,1])
            tmp2 = sorted(tmp2, key=lambda x: x[0])
            sm.append([tmp[0], tmp2[0]])
        else:
            sm.append([tmp[0], tmp[0]])
print(min(sm[-1])[0])
