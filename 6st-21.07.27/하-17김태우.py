from sys import stdin

number = list(map(int, stdin.readline().split()))

i = len(number)-1

while i > 0:
    for j in range(i):
        if number[j] > number[j+1]:
            t = number[j]
            number[j] = number[j+1]
            number[j+1] = t
    i -= 1
    
for n in number:
    print(n, end=" ")
