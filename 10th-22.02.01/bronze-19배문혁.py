## BOJ 10798

from pip import List


def list_padding(arr : List[List[str]], size : int) -> List[List[str]]:
	if size < 15:
		arr.extend(["+"] * (15 - size))
	return (arr)

arr = []

for i in range(5):
	arr.append(list(input()))
	list_padding(arr[i], len(arr[i]))

for j in range(15):
	for i in range(5):
		if arr[i][j].isalnum():
			print(arr[i][j], sep="", end="")
