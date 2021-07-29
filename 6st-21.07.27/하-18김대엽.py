A,B,C = map(int,input().split())
result = []
result.append(A)
result.append(B)
result.append(C)
result.sort()
for i in range(3):
    print(result[i],end=" ")