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

    def compute_height(self):
        mapper = self.getMapper()
        queue = [*mapper[-1]]
        new_queue = []
        height = 0
        while queue:
            par = queue.pop(0)
            if par in mapper:
                new_queue.extend(mapper[par])
            if not queue:
                height += 1
                queue.extend(new_queue)
                new_queue = []
        return height


def main():
    tree = TreeHeight()
    tree.read()
    tree.getMapper()
    print(tree.compute_height())


threading.Thread(target=main).start()
