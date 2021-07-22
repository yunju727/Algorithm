from sys import stdin
N = int(input())
A = list(map(int, stdin.readline().split()))
A.sort()    # 정렬

M = int(input())
B = list(map(int, stdin.readline().split()))

for i in B:
    a,b = 0,N-1
    while b - a >= 0:
        t = (a+b)//2    # mid 값
        if i == A[t]:   # 같은경우 1
            print(1)
            break
        elif i > A[t]:  # 찾는값이 더 큰 경우
            a = t + 1   # 좌측 인덱스 값 증가
        else:           # 찾는 값이 더 작은 경우
            b = t - 1   # 우측 인덱스 값 감소
    if b-a < 0:         # 찾지 못한 경우
        print(0)
