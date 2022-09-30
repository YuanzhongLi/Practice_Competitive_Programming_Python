class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.s1 = [] # stack1
        self.s2 = [] # stack2

    def enQueue(self, value: int) -> bool:
        if len(self.s1) + len(self.s2) == self.k:
            return False
        self.s1.append(value)
        return True

    def deQueue(self) -> bool:
        if len(self.s2) > 0:
            self.s2.pop()
            return True

        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())

        if len(self.s2) > 0:
            self.s2.pop()
            return True

        return False

    def Front(self) -> int:
        if len(self.s2) > 0:
            return self.s2[-1]

        if len(self.s1) > 0:
            return self.s1[0]

        return -1

    def Rear(self) -> int:
        if len(self.s1) > 0:
            return self.s1[-1]

        if len(self.s2) > 0:
            return self.s2[0]

        return -1

    def isEmpty(self) -> bool:
        return len(self.s1) + len(self.s2) == 0

    def isFull(self) -> bool:
        return len(self.s1) + len(self.s2) == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
