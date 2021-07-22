N = int(input())

a = 0
b = N
while True:
    t = (a+b)//2
    if N == t**2:
        print(t)
        break
    elif N < t**2:
        b = t
    elif N > t**2:
        a = t
