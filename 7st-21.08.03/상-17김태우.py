def f(k):
    if k == 1:
        return 0
    i = 1
    while 2**i < k:
        i+=1
    return not f(k-2**(i-1))

k = int(input())

if f(k):
    print(1)
else:
    print(0)
