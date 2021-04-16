class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def remove(self):
        prev = self.prev; next = self.next
        prev.next = next; next.prev = prev

class LinkedList:
    def __init__(self):
        head = Node(-1, -1); tail = Node(-1, -1)
        head.next = tail; tail.prev = head
        self.head = head
        self.tail = tail

    def get_by_key(self, key):
        cur = self.head
        while cur != self.tail:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def push_back(self, node):
        tail = self.tail
        prev = tail.prev
        prev.next =  node; node.prev = prev
        node.next = tail; tail.prev = node

    def update(self, key, value):
        cur = self.head.next
        while cur != self.tail:
            if cur.key == key:
                cur.val = value
                return True
            cur = cur.next
        return False

    def remove_by_key(self, key):
        cur = self.head.next
        while cur != self.tail:
            if cur.key == key:
                cur.remove()
                break
            cur = cur.next
        return


class MyHashMap:
    def __init__(self):
        self.mod = 2069
        self.buckets = [LinkedList() for _ in range(self.mod)]

    def put(self, key: int, value: int) -> None:
        key_mod = key % self.mod
        bucket = self.buckets[key_mod]
        if not bucket.update(key, value):
            new_node = Node(key, value)
            bucket.push_back(new_node)

    def get(self, key: int) -> int:
        key_mod = key % self.mod
        bucket = self.buckets[key_mod]
        return bucket.get_by_key(key)

    def remove(self, key: int) -> None:
        key_mod = key % self.mod
        bucket = self.buckets[key_mod]
        bucket.remove_by_key(key)
