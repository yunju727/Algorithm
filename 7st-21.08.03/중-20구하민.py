import sys

def str_check(s,n):
    x = 0;y=0
    global check_1;global check_0
    for i in range(n):
        x += s[i].count(1)
        y += s[i].count(0)
    if x == n**2 : check_1 += 1
    elif y == n**2 : check_0 += 1
    else: return str_divide(s,n)

def str_divide(s,n):
    if len(s) <= 1:return
    else:
        C = [];D=[];E=[];F=[]
        for i in range(n//2):
            C.append(s[i][:n//2]) 
            D.append(s[i][n//2:2*(n//2)])
            E.append(s[n//2+i][:n//2])
            F.append(s[n//2+i][n//2:2*(n//2)])
        str_check(C,n//2)
        str_check(D,n//2)
        str_check(E,n//2)
        str_check(F,n//2)


n = int(input())
check_0 = 0
check_1 = 0

A = []
for i in range(n) : A.append(list(map(int, sys.stdin.readline().rstrip().split())))
str_check(A,n)

print(check_0)
print(check_1)
