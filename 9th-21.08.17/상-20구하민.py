# DFS와 BFS
# https://www.acmicpc.net/problem/1260

from collections import deque
import sys

def DFS(graph,v):
    visit=[]
    stack = []
    
    stack.append(v)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)

            if len(graph[node]) >= 2:
                graph[node].sort(reverse=True)
            stack.extend(graph[node])
    return visit

def BFS(graph,v):
    visit=[]
    queue = deque()

    queue.append(v)
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit

n,m,v = map(int, sys.stdin.readline().split())
graph={}

for i in range(n):graph[i+1] = []
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
print(' '.join(map(str, DFS(graph,v))))

for i in graph.keys():
    graph[i].sort()

print(' '.join(map(str, BFS(graph,v))))
