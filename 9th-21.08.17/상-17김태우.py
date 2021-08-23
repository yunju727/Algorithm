from sys import stdin

def dfs(graph, start_node):
    stack = list()
    visit = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(reversed(graph[node]))

    return visit

def bfs(graph, start_node):
    queue = list()
    visit = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit

N, M, V = map(int,stdin.readline().split())

li = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int,stdin.readline().split())
    li[a].append(b)
    li[b].append(a)

li2 = [[] for _ in range(N+1)]
for i in range(len(li)):
    li2[i] = sorted(li[i])

li_dfs = dfs(li2,V)
li_bfs = bfs(li2,V)

for i in li_dfs:
    print(i,end=" ")
print()
for i in li_bfs:
    print(i, end=" ")
