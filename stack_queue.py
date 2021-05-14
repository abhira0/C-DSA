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


class StackOp:
    @staticmethod
    def parenthesisMatching(string: str):
        """If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes). Otherwise, output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing brackets, output the 1-based index of the first unmatched opening bracket

        Returns:
            Success: If balanced
            index  : if imbalanced
        """
        mapper = {"{": "}", "[": "]", "(": ")"}
        s = Stack()
        for ind, c in enumerate(string):
            if c in mapper:
                s.push([c, ind + 1])
            elif c in mapper.values():
                try:
                    popped = s.pop()
                except:
                    return ind + 1
                if mapper[popped[0]] != c:
                    return ind + 1
        return "Success" if s.isEmpty() else s.pop()[1]


class Queue:
    def __init__(self) -> None:
        self.queue = []
        self.len = 0

    def enqueue(self, key):
        self.stack.append(key)
        self.len += 1

    def dequeue(self):
        if self.stack:
            self.len -= 1
            return self.stack.pop(0)

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
        elif self.minstack.top() < key:
            self.minstack.push(self.minstack.top())
            self.maxstack.push(key)
        else:
            self.maxstack.push(self.maxstack.top())
            self.minstack.push(key)

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
