def func(x,y,n):
        if ((x//n)%3 == 1) and ((y//n)%3 == 1):
            list[x][y] = " "
        else:
            if n == 1:
                pass
            else:
                func(x,y,n//3)



n = int(input())

list = [['*' for col in range(n)] for row in range(n)]

for x in range(len(list)):
    for y in range(len(list)):
        func(x,y,n)

for i in range(len(list)) :
    for j in range(len(list)) :
        print(list[i][j], end='')
    print()

