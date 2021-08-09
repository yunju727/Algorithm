from sys import stdin

white = 0
blue = 0
sq = list()

def func(start, start2, N):    # 자르기  list[ind][start:end] N->개수
    global blue, white

    check = 0
    for i in range(start,start+N):
        check += sum(sq[i][start2:start2+N])

    if N == 2 and check!=4:
        blue += check
        if check==0:
            white+=1
        else:
            white += 4 - check
    elif check == N**2:
        blue += 1
    elif check == 0:
        white += 1
    else:
        func(start, start2, N//2)    # 좌상단
        func(start, start2+N//2, N//2)     # 우상단
        func(start+N//2, start2, N//2)   # 좌하단
        func(start+N//2, start2+N//2, N//2)     # 우하단

n = int(input())    # 변의 길이

for i in range(n):
    sq.append(list(map(int, stdin.readline().split())))

func(0,0,n)

print(white)
print(blue)
