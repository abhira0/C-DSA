class Queue:
    def __init__(self, maxsize: int = 99999) -> None:
        self.queue = []
        self.len = 0
        self.maxsize = maxsize

    def enqueue(self, key):
        print(self.len, self.ma)
        if self.len >= self.maxsize:
            return -1
        self.queue.append(key)
        self.len += 1
        return 1

    def dequeue(self):
        if self.queue:
            self.len -= 1
            return self.queue.pop(0)

    def isEmpty(self):
        return self.len == 0

    def nextUp(self):
        return self.queue[0]


def process(requests, size):
    q = Queue(size)
    lost_ind = []
    response = []
    time = 0
    processing_req = None
    wait_until = 0
    req_ind = 0
    while True:
        while requests[req_ind][0] == time:
            if q.enqueue(requests[req_ind]) == -1:
                lost_ind.append(req_ind)
            req_ind += 1
        if not processing_req and not q.isEmpty() and wait_until <= time:
            processing_req = q.dequeue()
            wait_until = time + processing_req[1]

        time += 1


def main():
    size, n = map(int, input().split())
    if n == 0:
        return None
    requests = []
    for _ in range(n):
        a, p = map(int, input().split())
        requests.append([a, p])
    process(requests, size)


main()
