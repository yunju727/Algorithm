N = int(input())

first = 1
last = N

while(True):
    middle = (first+last) // 2
    if middle**2 == N:
        print(middle)
        break
    elif middle**2 > N:
        last = middle - 1
    elif middle**2 < N:
        first = middle + 1