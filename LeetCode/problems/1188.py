from collections import deque
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.data = deque([])
        self.cap = capacity

    def enqueue(self, element: int) -> None:
        while True:
            if len(self.data) < self.cap:
                self.data.append(element)
                break

    def dequeue(self) -> int:
        while True:
            if len(self.data) > 0:
                return self.data.popleft()

    def size(self) -> int:
        return len(self.data)
