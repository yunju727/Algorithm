count = 0

def hanoi(n,f,t,s):
    global count
    count += 1
    if n == 1:
        print(f"{f} {t}")
    else:
        hanoi(n-1, f, s, t)
        print(f"{f} {t}")
        hanoi(n-1, s, t, f)

n = int(input())
print(2**n-1)
hanoi(n,1,3,2)
