n = int(input())
stairs=[0 for i in range(301)]
for i in range(1,n+1) : 
    stairs[i] = int(input())
    
DP = [0 for i in range(301)]

DP[1] = stairs[1]
DP[2] = max(DP[1]+stairs[2], stairs[2])
DP[3] = max(DP[1]+stairs[3], DP[0]+stairs[2]+stairs[3])

for i in range(3, n+1) : 
    DP[i] = max(DP[i-2]+stairs[i], DP[i-3]+stairs[i-1]+stairs[i])
    
print(DP[n])
