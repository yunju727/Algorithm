n = int(input())    # n번째 피보나치 수

f = [0,1]   # 피보나치 수를 위한 리스트

if n == 0 or n == 1:
    print(n)
else:
    for i in range(2,n+1):  # n번째 까지 탐색
        f.append(f[i-1]+f[i-2])
    print(f[n])
