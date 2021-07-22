from sys import stdin
N = int(input())
A = list(map(int, stdin.readline().split()))
A.sort()

M = int(input())
B = list(map(int, stdin.readline().split()))

for i in B:
    a,b = 0,N-1
    while b - a >= 0:
        t = (a+b)//2
        if i == A[t]:
            print(1)
            break
        elif i > A[t]:
            a = t + 1
        else:
            b = t - 1
    if b-a < 0:
        print(0)
