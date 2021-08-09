from sys import stdin

li = list()

def bs(N,p):    # 정렬 전 나누기
    t = N//p
    i = 0
    while i < N-t+1:
        li[i:i+t] = sortt(i,i+t)
        i += t


def sortt(st,en):    # 정렬 후 출력
    global li
    return sorted(li[st:en])

N = int(input())
li = list(map(int, stdin.readline().split()))
p = int(input())

bs(N,p)
for i in range(len(li)):
    print(li[i],end=" ")
