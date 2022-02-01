## BOJ 7576
# 문제의 선조건 : 1 (토마토 있음)은 최소 1개가 보장된다.
# 기존 BFS와의 차이점 : 시작점이 정해져 있지 않음. 
# 해결책 : 초기화 느낌, 시작점이 될 조건에 있는 것들 모두 큐에 넣고 bfs 진행
from pip import List
from collections import deque


# n, m 을 white space를 구분자로 하여 입력 받기
m, n = map(int, input().split())

# 2차원 리스트 형태로 토마토 정보 입력
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))

# 상하좌우 정의 (상 : -y) (하 : +y)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 여부 초기화
visited = [[False] * m for _ in range(n)]

# BFS 구현  (문제 명세까지 포함된 BFS)
def bfs(graph : List[List[int]], n : int, m : int, visited : List[List[bool]]):# -> List[List[int]]:
	# 저장될 때부터 익어있는 상태 (예외처리)
	# if 0 not in graph:
	# 	print(0)
	# 	return

	# Queue 구현에 deque(데크) 라이브러리 사용, dequeue 연산이랑 다름
	queue = deque()
	# 초기화
	for x in range(n):
		for y in range(m):
			if graph[x][y] == 1:
				queue.append((x, y))
				visited[x][y] = True
		# print(visited[x])
	# print(queue)
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or nx >= n  or ny < 0 or ny >= m:
				continue
			if graph[nx][ny] == -1:
				visited[nx][ny] = True
				continue
			if graph[nx][ny] == 0 and not visited[nx][ny]:
				graph[nx][ny] += graph[x][y] + 1
				queue.append((nx, ny))
				visited[nx][ny] = True

	if any(0 in l for l in graph): # if any(False in l for l in visited): 로도 가능
		print(-1)
		return
	else:
		print(max(map(max, graph)) - 1)

# bfs 호출
bfs(graph, n, m , visited)