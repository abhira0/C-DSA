# python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeHeight:
    def getMapper(self):
        mapper = {}
        for ind, p in enumerate(self.parent):
            mapper[p] = mapper.get(p, []) + [ind]
        return mapper

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    # def read(self):
    #     self.parent = list(map(int, "4 -1 4 1 1".split(" ")))
    #     self.n = len(self.parent)

    def compute_height(self):
        mapper = self.getMapper()
        queue = [*mapper[-1]]
        height = 0
        print(mapper)
        while queue:
            par = queue.pop(0)
            if not queue:
                height += 1
            try:
                queue.extend(mapper[par])
            except:
                ...
            print(height, queue)
        return height


def main():
    tree = TreeHeight()
    tree.read()
    tree.getMapper()
    print(tree.compute_height())


threading.Thread(target=main).start()
