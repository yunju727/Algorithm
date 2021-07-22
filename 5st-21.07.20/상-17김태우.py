from sys import stdin

n = int(input())

li = list(map(int, stdin.readline().split()))
li.sort()   # 정렬

min = abs(li[0] + li[-1])   # 최초 최소값
ne = 0
po = len(li)-1  # 최초 최소값의 인덱스
a = 0
b = len(li)-1
while a < b:    # 오름차순 정렬 -> 앞 인덱스가 뒤 인덱스를 넘기 전까지
    t = li[a] + li[b]   # 두 합
    if min > abs(t):    # 절대값이 최소값보다 작은경우
        min = abs(t)
        ne = a
        po = b
    else:   
        if t > 0:   # 0 보다 큰 경우 우측 인덱스 감소
            b-=1
        else:       # 0 보다 작은 경우 좌측 인덱스 감소
            a+=1

print(f"{li[ne]} {li[po]}")
