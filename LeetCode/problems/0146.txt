### mid
### use OrderedDict
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.used = 0
        self.cap = capacity
        self.od = OrderedDict()

    def get(self, key: int) -> int:
        if self.od.get(key, None) == None:
            return -1
        else:
            self.od.move_to_end(key)
            return self.od[key]

    def put(self, key: int, value: int) -> None:
        if self.od.get(key, None) == None:
            if self.used == self.cap:
                remove_key = next(iter(self.od.keys())
                del od[remove_key]
                self.od[key] = value
            else:
                self.od[key] = value
                self.used += 1
        else:
            self.od.move_to_end(key)
            self.od[key] = value

### use d linked list
class Node:
    def __init__(self, val=0, key=-1, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        self.used = 0
        self.cap = capacity
        self.mp = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if self.mp.get(key, None) == None:
            return -1
        else:
            node = self.mp[key]
            self.to_end(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if self.mp.get(key, None) == None:
            node = Node(value, key)
            if self.used == self.cap:
                top = self.head.next
                self.delete(top)
                self.add(node)
                self.mp[key] = node
            else:
                self.add(node)
                self.mp[key] = node
                self.used += 1
        else:
            node = self.mp[key]
            node.val = value
            self.to_end(node)

    def delete(self, node):
        key = node.key
        del self.mp[key]
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add(self, node):
        key = node.key
        last = self.tail.prev
        last.next = node
        node.prev = last
        self.tail.prev = node
        node.next = self.tail
        self.mp[key] = node

    def to_end(self, node):
        self.delete(node)
        self.add(node)
