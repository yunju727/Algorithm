from sys import stdin

count = 0   # 연결된 개수

def f(key): # key가 있는 곳을 탐색
    global count
    count += 1
    check[key] = 1  # 탐색 완료
    for t in li[key]:   # key값 위치의 리스트
        if check[t] == 0:   # 탐색한 적이 없음
            f(t)    # t-> key값으로 탐색한 위치의 원소 값으로 함수 f의 key값으로 전달.

n = int(input())    # 컴퓨터 대수
s = int(input())    # 연결 쌍 개수

li = [[] for _ in range(n+1)]
check = [0] * (n+1)

for i in range(s):
    a, b = map(int,stdin.readline().split())
    li[a].append(b)
    li[b].append(a)

f(1)

print(count-1)
