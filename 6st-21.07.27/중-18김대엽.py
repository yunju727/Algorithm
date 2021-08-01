N = int(input())   # 대회참가 학생 수

studentlist = []

for _ in range(N):
    student = list(map(int, input().split()))
    studentlist.append(student)
#확인용 출력 : print(studentlist)
studentlist = sorted(studentlist, key = lambda x: -x[2])   # -x[2] : x[2]번째 인자를 기준으로 내림차순 정렬

if studentlist[0][0] == studentlist[1][0]:
    print(*studentlist[0][:2])
    print(*studentlist[1][:2])
    print(*studentlist[3][:2])
else:
    print(*studentlist[0][:2])
    print(*studentlist[1][:2])
    print(*studentlist[2][:2])