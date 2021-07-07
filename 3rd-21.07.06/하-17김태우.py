def B(n):
    if n == 1:
        print(n, end="")
    else:
        B(n//2)
        print(n%2, end="")

N = int(input())
B(N)