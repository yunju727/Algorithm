# 세 수 정렬하기
# 입력
three_number = input().split()

# 형변환
for i in range(3):
    three_number[i] = int(three_number[i])

# 정렬
three_number.sort()

# 결과 출력
print(three_number[0], three_number[1], three_number[2])
