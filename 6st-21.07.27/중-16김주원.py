# 아시아 정보 올림피아드 문제 
student_num = int(input())
student = []
nation = []

for i in range(student_num):
    student.append(input().split())

for i in range(student_num):
    student[i][2] = int(student[i][2])
    student[i][0] = int(student[i][0])
    student[i] = tuple(student[i])
    
student.sort(key = lambda score: score[2], reverse=True)

for i in range(len(student)):
    nation.append(student[i][0])

nation_set = set(nation)
nation_set = list(nation_set)
checknation_num = 0
count = 0
num = 0
temp = student[0][0]

while True :

    if checknation_num <= 1: 
        print(student[num][0], student[num][1])
        if temp == student[num][0]:
            checknation_num+=1
        count +=1 
    else : 
        nation_set.remove(temp)
        third=[]
        for i in range(len(nation_set)):
            third.append(nation.index(nation_set[i]))
        temp = student[third[0]][2]
        num = third[0]
        for i in range(len(third)):
            if student[third[i]][2] > temp :
                temp = student[third[i]][2]
                num = third[i] 
        print(student[num][0], student[num][1])
        count +=1 
    num +=1

    if count == 3 :
        break
        
