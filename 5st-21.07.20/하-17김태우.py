N = int(input())

a = 0
b = N
while True:
    t = (a+b)//2
    if N == t**2: # 제곱근에 해당
        print(t)
        break
    elif N < t**2:  # 제곱근 값이 작은경우
        b = t
    elif N > t**2:  # 제곱근 값이 큰 경우
        a = t
