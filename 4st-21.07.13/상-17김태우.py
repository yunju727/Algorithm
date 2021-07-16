dic = {}

def f():
    d = sorted(dic) # 제한 시간
    al = dic.values()

    start = d[0] - dic[d[0]]    # 제한 시간 - 소요 시간 = 최대시작 시간
    temp = start
    for i in range(len(dic)):
        temp = temp + dic[d[i]]    # i번째 진행한 시간
        if temp > d[i]:    # Si를 넘긴 경우
            di = temp - d[i]   # 초과한 시간
            start -= di
            temp -= di
        if start < 0:
            print("-1")
            return
    print(start)


N = int(input())    # 일의 수

for i in range(N):
    s = input().split()
    dic[int(s[1])] = int(s[0])

f()
