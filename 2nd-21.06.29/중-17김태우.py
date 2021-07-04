import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1


N = int(sys.stdin.readline())  # 명령어 수

s = Stack()

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        s.push(int(command[1]))
    elif command[0] == "pop":
        print(s.pop())
    elif command[0] == "size":
        print(s.size())
    elif command[0] == "empty":
        print(s.empty())
    elif command[0] == "top":
        print(s.top())
    else:
        print("Wrong input")