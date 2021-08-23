from sys import stdin

def even(row, col, last): # 짝수
    count = 0
    if col == 0:  # 열의 첫번째 원소
        count -= 1
        if m[row - 1][col] == '#':  # 좌상단이 땅
            count -= 2
        if m[row - 1][col + 1] == '#':  # 우상단이 땅
            count -= 2
        if m[row][col + 1] == '#':  # 우측이 땅
            count -= 1
    elif col == M - 1:  # 열의 마지막
        if last == 1:
            count -= 2
        else:
            count -= 3
        if m[row - 1][col] == '#':  # 좌상단 땅
            count -= 2
        if m[row][col - 1] == '#':  # 좌측 땅
            count -= 1
    else:
        if m[row][col - 1] == '#':  # 좌
            count -= 1
        if m[row - 1][col] == '#':
            count -= 2
        if m[row - 1][col + 1] == '#':
            count -= 2
        if m[row][col + 1] == '#':
            count -= 1
    return count

def odd(row, col, last):  # 홀수
    count = 0
    if col == 0:  # 열의 첫번째 원소
        if last == 1:
            count -= 2
        else:
            count -= 3
        if m[row - 1][col] == '#':  # 우상단이 땅
            count -= 2
        if m[row][col + 1] == '#':  # 우측이 땅
            count -= 1
    elif col == M - 1:  # 열의 마지막
        count -= 1
        if m[row - 1][col-1] == '#':  # 좌상단 땅
            count -= 2
        if m[row-1][col] == '#':  # 우상단 땅
            count -= 2
        if m[row][col-1] == '#':  # 좌측 땅
            count -= 1
    else:
        if m[row][col - 1] == '#':  # 좌
            count -= 1
        if m[row - 1][col] == '#':
            count -= 2
        if m[row - 1][col - 1] == '#':
            count -= 2
        if m[row][col + 1] == '#':
            count -= 1
    return count

N,M = map(int, stdin.readline().split())    # 지도의 세로, 가로 크기

m = list()
for i in range(N):  # 지도 정보 저장
    m.append(list(input()))

count = 0   # 해변의 개수

for row in range(N):    # 행 -> 세로 크기만큼 반복
    for col in range(M):    # 열 -> 가로 크기만큼 반복
        if M == 1:
            if N == 1:  # 행, 열 모두 길이가 1
                break
            else:   # 열이 1
                if row == 0:
                    if m[row][col] == '#':
                        count += 1
                elif row == N-1:    # 마지막 행
                    if m[row][col] == '#':
                        count += 1
                        if m[row-1][col] == '#':
                            count -= 2
                else:
                    if m[row][col] == '#':
                        count += 2
                        if m[row-1][col] == '#':
                            count -= 2
                continue
        if row == 0:  # 첫 번째 행인 경우
            if m[row][col] == '#':  # 땅인 경우
                if N == 1:  # 행 최대가 1
                    count += 2
                    if col == 0:  # 열의 첫번째 원소인 경우
                        count -= 1
                        if m[row][col + 1] == '#':  # 우측이 땅인 경우
                            count -= 1
                    elif col == M-1:    # 열의 마지막 원소
                        count -= 1
                        if m[row][col-1] == '#':    # 좌측이 땅인 경우
                            count -= 1
                    else:
                        if m[row][col-1] == '#':    # 좌측이 땅
                            count -= 1
                        if m[row][col+1] == '#':    # 우측이 땅
                            count -= 1
                else:   # 행 크기가 2 이상
                    count += 4
                    if col == 0:  # 열의 첫번째 원소인 경우
                        count -= 2
                        if m[row][col + 1] == '#':  # 우측이 땅인 경우
                            count -= 1
                    elif col == M-1:    # 열의 마지막 원소
                        count -= 1
                        if m[row][col - 1] == '#':  # 좌측이 땅
                            count -= 1
                    else:
                        if m[row][col-1] == '#':    # 좌측이 땅
                            count -= 1
                        if m[row][col+1] == '#':    # 우측이 땅
                            count -= 1
        else:
            if (row+1)%2 == 0:    # 짝수번째 행
                if m[row][col] == '#':  # 땅인 경우
                    if row == N-1:    # 마지막 행
                        count += 4
                        count += even(row,col,1)
                    else:   # 마지막 행 X
                        count += 6
                        count += even(row,col,0)
            else:   # 홀수번째 행
                if m[row][col] == '#':
                    if row == N - 1:  # 마지막 행
                        count += 4
                        count += odd(row,col,1)
                    else:
                        count += 6
                        count += odd(row,col,0)
print(count)
