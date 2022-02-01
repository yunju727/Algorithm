## BOJ 2579

# 2021D
import copy
from pip import List


def list_padding(arr : List[int], size : int) -> List[int]:
	if size <= 301:
		arr.extend([0] * (301 - size))
	return (arr)

n = int(input())
value = [
	int(input())
	for _ in range(n)
]
list_padding(value, len(value))
dp = copy.deepcopy(value) # 명시적 코드 귀찮으면 dp = value[:] (마찬가지로 깊은 복사, 값 복사)
dp[1] += value[0]
dp[2] += max(value[1], value[0])
for i in range(3, n):
	dp[i] += max(dp[i-2], dp[i-3] + value[i-1])
	# print("{} : {}".format(i, dp[i]))

print(dp[n-1])

#2021C
from pip import List


def climb_cost(n : int, w : List[int]) -> int:
    dp[1] = w[1]
    dp[2] = w[2] + w[1]
    
    for i in range(3,n+1): #이제 FF는 안돼. F 또는 S. 이전에 F였다면 S. 따라서 삼항이 필요하다.
        dp[i] = w[i] + max(dp[i-2], w[i-1] + dp[i-3])
        # #추적표
        # print("dp[{}]:{} = {} + {}".format(i, dp[i], w[i], max(dp[i-2], w[i-1] + dp[i-3]))) 
        
    print(dp[n])

dp = [0] * 301
n = int(input())

w =[0] * 301 #계단 수와 index를 일치
for i in range(1, n+1):
    w[i] = int(input())
climb_cost(n, w)
