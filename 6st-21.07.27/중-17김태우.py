from sys import stdin

class student:
    def __init__(self,N,S,C):
        self.N_num = N
        self.S_num = S
        self.score = C
    def __str__(self):
        return '{} {}'.format(self.N_num,self.S_num)


n = int(input())    # 학생 수

li = list()
for i in range(n):
    number = list(map(int, stdin.readline().split()))
    li.append(student(number[0],number[1],number[2]))

while i > 0:
    for j in range(i):
        if li[j].score < li[j+1].score:
            t = li[j]
            li[j] = li[j+1]
            li[j+1] = t
    i -= 1

count = [0]*n
pcount = 0

for t in li:
    if count[t.N_num] < 2 and pcount < 3:
        print(t)
        pcount+=1
        count[t.N_num]+=1
    else:
        continue
