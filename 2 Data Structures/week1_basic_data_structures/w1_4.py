import sys


class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.len = 0

    def push(self, key):
        self.stack.append(key)
        self.len += 1

    def pop(self):
        if self.stack:
            self.len -= 1
            return self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def isEmpty(self):
        return self.len == 0


class MinMaxStack:
    """Design a stack that supports push, pop, top, and retrieving the minimum or maximum element in constant time."""

    def __init__(self) -> None:
        self.stack = Stack()
        self.minstack = Stack()
        self.maxstack = Stack()

    def push(self, key):
        self.stack.push(key)
        if self.minstack.isEmpty():
            self.minstack.push(key)
            self.maxstack.push(key)
        else:
            self.maxstack.push(max(self.maxstack.top(), key))
            self.minstack.push(min(self.minstack.top(), key))

    def pop(self):
        self.minstack.pop()
        self.maxstack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack.top()

    def getMin(self) -> int:
        return self.minstack.top()

    def getMax(self) -> int:
        return self.maxstack.top()

    def isEmpty(self):
        return self.stack.isEmpty()

    def display(self):
        print(f"stack:    {self.stack.stack}")
        print(f"maxstack: {self.maxstack.stack}")
        print(f"minstack: {self.minstack.stack}")


if __name__ == "__main__":
    stack = MinMaxStack()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.getMax())
        else:
            assert 0
