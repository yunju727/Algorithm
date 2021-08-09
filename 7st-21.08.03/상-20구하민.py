# 투에-모스 문자열
# https://www.acmicpc.net/problem/18222


def check(n,x):
    global a
    if n <= 2:
        if a % 2 != 0 or a == 1:
            if n == 1:print(1)
            else:print(0)
        else:
            if n == 1:print(0)
            else:print(1)
        return
    if n > x//2:#뒤에 있는 경우
        a += 1
        check(n - x//2,x//2)
    else:check(n,x//2)


n = int(input())
a = 0
x = 1
while True:
    if n <= x:break
    x = x*2
check(n,x)
