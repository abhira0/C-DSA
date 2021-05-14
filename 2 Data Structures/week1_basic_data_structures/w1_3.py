class Queue:
    def __init__(self, maxsize: int = 99999) -> None:
        self.queue = []
        self.len = 0
        self.maxsize = maxsize

    def enqueue(self, key):
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


class Request:
    def __init__(self, arrival, processing) -> None:
        self.arrival = arrival
        self.processing = processing
        self.began_at = -1
        self.completed_at = -1


class RequestList:
    def __init__(self) -> None:
        self.ind = 0
        self.requests = []
        self.len = 0

    def addRequest(self, req: Request):
        self.requests.append(req)
        self.len += 1

    def getNext(self) -> Request:
        if self.ind < self.len:
            return self.requests[self.ind]

    def isCompleted(self):
        return self.ind == self.len


def process(requests: RequestList, size):
    q = Queue(size)
    time = 0
    processing_req: Request = None
    wait_until = -1
    while True:
        while requests.getNext() and requests.getNext().arrival == time:
            q.enqueue(requests.getNext())
            requests.ind += 1
        if wait_until == time and processing_req:
            processing_req.completed_at = time
            processing_req = None
        while not processing_req and not q.isEmpty() and wait_until <= time:
            processing_req = q.dequeue()
            wait_until = time + processing_req.processing
            processing_req.began_at = time
        time += 1
        if requests.isCompleted() and q.isEmpty():
            break
    for resp in requests.requests:
        print(resp.began_at)


def main():
    size, n = map(int, input().split())
    if n == 0:
        return None
    requests = RequestList()
    for _ in range(n):
        a, p = map(int, input().split())
        requests.addRequest(Request(a, p))
    process(requests, size)


main()
