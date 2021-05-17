import os
from copy import deepcopy

from termcolor import cprint


class Queue:
    def __init__(self, maxsize: int = 99999) -> None:
        self.queue = []
        self.len = 0
        self.maxsize = maxsize

    def enqueue(self, key, processing_req, verbose: bool = False):
        if processing_req:
            maxi = self.maxsize - 1
        else:
            maxi = self.maxsize
        if self.len >= maxi:
            if verbose:
                print(f"DROPPING {key.arrival} {key.processing}, MAXSIZE: {maxi}")
            return -1
        if verbose:
            print(f"ADDING {key.arrival} {key.processing}\tMAXSIZE: {maxi}")
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
        if self.queue:
            return self.queue[0]
        else:
            return None

    def forcedEnqueue(self, key, verbose: bool = False):
        if verbose:
            print(f"Forced Enqueue: {key.arrival} {key.processing}")
        self.queue.append(key)
        self.len += 1
        return 1

    def copy(self):
        return deepcopy(self)


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


def Disclay(wait_until, time, processing_req):
    print("\t\t", wait_until, time, end=" ")
    if processing_req:
        print(
            processing_req.arrival,
            processing_req.processing,
            processing_req.began_at,
            processing_req.completed_at,
        )
    else:
        print("None")


def disSlay(wait_until, time, prev_q, q):
    print(
        "\t",
        time,
        wait_until,
        [(i.arrival, i.processing, i.began_at, i.completed_at) for i in prev_q.queue],
        " -> ",
        [(i.arrival, i.processing, i.began_at, i.completed_at) for i in q.queue],
    )


def process(requests: RequestList, size, verbose: bool = False):
    q = Queue(size)
    time = 0
    buffer_size = 0
    last_proc_ind = 0
    proc_req: Request = None
    while True:
        print(f"Time: {time}")
        print(requests.getNext().arrival, time) if requests.getNext() else None
        while requests.getNext() and requests.getNext().arrival == time:
            print("\t", buffer_size, size)
            if buffer_size < size:
                proc_req = requests.getNext()
                last_proc_req = proc_req
                proc_req.began_at = time
                proc_req.completed_at = time + proc_req.processing
                buffer_size += 1
            if last_proc_req.completed_at == time:
                buffer_size -= 1
            requests.ind += 1

        time += 1
        if requests.ind == requests.len:
            break

    return requests.requests


def main(verbose: bool = False):
    size, n = map(int, input().split())
    if n == 0:
        return None
    requests = RequestList()
    for _ in range(n):
        a, p = map(int, input().split())
        requests.addRequest(Request(a, p))
    resps = process(requests, size, verbose)
    for resp in resps:
        print(resp.began_at)


def main(chan, verbose: bool = False):
    requests = RequestList()
    ipl = [i.strip() for i in chan.split("\n") if i.strip()]
    size, n = map(int, ipl.pop(0).split())
    for ip in ipl:
        a, p = map(int, ip.split())
        requests.addRequest(Request(a, p))
    proc_resp = process(requests, size, verbose)
    if proc_resp:
        return "\n".join([str(i.began_at) for i in proc_resp]) + "\n"
    else:
        return ""


for i in range(1, 15):
    ii = str(i).zfill(2)
    filename = f"../week1_basic_data_structures/3_network_simulation/tests/{ii}"
    with open(filename, "r") as f:
        chan = f.read()
    with open(f"{filename}.a", "r") as f:
        expected_result = f.read()
    actual_result = main(chan)
    if expected_result != actual_result:
        print("-" * 20)
        main(chan, verbose=True)
        print("-" * 20)
        print(f"Testcase: {i}")
        print(chan)
        print("Expected")
        print(expected_result)
        print("Actual")
        print(actual_result)
        break
else:
    print("Done")
