def f(T):
    A = 300
    B = 60
    C = 10
    countA, countB, countC = 0,0,0

    if T%10 > 0:    # T가 1초 단위가 있는 경우
        print("-1")
    else:
        while T>0:
            if T>=A:
                T -= A
                countA += 1
            elif T>=B:
                T -= B
                countB += 1
            elif T>=C:
                T -= C
                countC += 1
        print(f"{countA} {countB} {countC}")

T = int(input())
f(T)
