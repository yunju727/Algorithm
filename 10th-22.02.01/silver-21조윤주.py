n=int(input())
stair=[]
for i in range(n):
    stair.append(int(input()))

def jump(a):
    S=[]
    for i in range(2*len(a)-1):
        S.append([0,0])
    S[0]=[a[0],1]
    
    if len(a)>=2:
        S[1]=[a[1],1]
        S[2]=[S[0][0]+a[1],2]
    else:return S[0][0]
    
    for i in range(2,len(a)):
        L,R=2*i-1,2*i
        if L==3:
            S[L]=[S[0][0]+a[i],1]
        else:
            L_max=max(S[L-2*2][0],S[L-2*2+1][0])
            S[L]=[L_max+a[i],1]
        S[R]=[S[R-3][0]+a[i],2]
    return max(S[-1][0],S[-2][0])

print(jump(stair))