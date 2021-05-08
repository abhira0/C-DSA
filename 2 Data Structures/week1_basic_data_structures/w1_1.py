def getInput():
    return input().strip()


class Stack:
    def __init__(self):
        self.values = []
        self.length = 0

    def push(self, val, ind):
        self.values.append([val, ind])
        self.length += 1

    def pop(self):
        if self.values:
            self.length -= 1
            return self.values.pop()
        else:
            raise ("Empty Stack")

    def isEmpty(self):
        return self.length == 0

    def len(self):
        return self.length


def Solution():
    mapper = {"{": "}", "[": "]", "(": ")"}
    s = Stack()
    for ind, c in enumerate(getInput()):
        if c in mapper:
            s.push(c, ind + 1)
        elif c in mapper.values():
            try:
                popped = s.pop()
            except:
                return ind + 1
            if mapper[popped[0]] != c:
                return ind + 1
    if s.isEmpty():
        return "Success"
    else:
        return s.pop()[1]


print(Solution())