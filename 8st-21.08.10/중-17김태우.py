n = int(input())

f = [0, 1, 1, 1]

for i in range(4, n+1):
    tmp = list()
    if i % 3 == 0:
        tmp.append(f[i//3])
    if i % 2 == 0:
        tmp.append(f[i//2])
    tmp.append(f[i-1])
    f.append(1 + min(tmp))
if n == 1:
    print(0)
else:
    print(f[n])
