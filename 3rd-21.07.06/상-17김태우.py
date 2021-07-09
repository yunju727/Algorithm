def S(n) :
    size = 3
    k = 1
    if n == 1:
        print("m")
    elif n <= 3:
        print("o")
    else:
        while size <= n:
            size = size*2 + k + 3
            k = k+1

        k = k-1
        mid = (size-3-k)//2 + 1

        if n == mid:
            print("m")
        elif mid < n and n <= mid+k+2:
            print("o")
        else:
            S(n-size+(mid-1))

N = int(input())
S(N)
