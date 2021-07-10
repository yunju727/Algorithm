def f(n,c):
    if int(n) < 10:
        print(c)
        if int(n)%3 == 0:
            print("YES")
        else:
            print("NO")
    else:
        c += 1
        sum = 0
        for i in range(len(n)):
            sum = sum + int(n[i])
        f(str(sum),c)

n = input()
f(n,0)
