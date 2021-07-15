def f(S):
    if S[0] == '1':
        check = 1
        a = 1
        b = 0
    else:
        check = 0
        a = 0
        b = 1
    for i in range(1,len(S)):
        if S[i] != S[i-1]:
            if check == 1:
                b += 1
                check = 0
            else:
                a += 1
                check = 1
    if a <= b:
        print(a)
    else:
        print(b)

S = input()
f(S)
