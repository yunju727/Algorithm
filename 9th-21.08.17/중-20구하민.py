# 바이러스
# https://www.acmicpc.net/problem/2606

def g(graph):
    visit = []
    stack = [1]
    
    while stack:
        node = stack.pop()
        for i in graph:
            if node == i[0] and i[1] not in visit:
                stack.append(i[1])
                visit.append(i[1])
            elif node == i[1] and i[0] not in visit:
                stack.append(i[0])
                visit.append(i[0])
            else:pass
    return visit

n = int(input())
m = int(input())
graph = list()
for i in range(m):
    graph.append(list(map(int, input().split())))

network = g(graph)
print(len(network)-1)
