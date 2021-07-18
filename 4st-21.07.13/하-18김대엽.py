T = int(input())
A,B,C = 0,0,0

if T%10 == 0:
    A = T//300
    T = T-A*300

    B = T//60
    T = T-B*60

    C = T//10
    C - T-C*10
    print(A, B, C)
else:
    print(-1)