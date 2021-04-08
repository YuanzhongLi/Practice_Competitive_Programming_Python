# 460. LFU Cache
class Node:
    def __init__(self, val, prev=None, next=None, key=None, freq=0, nodelist=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.key = key
        self.freq = freq
        self.nodelist=nodelist

class NodeList:
    def __init__(self, freq=-1, prev=None, next=None):
        self.freq = freq
        self.size = 0
        self.prev = prev
        self.next = next
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail; self.tail.prev = self.head

    def put_back(self, node):
        node.nodelist = self
        tail = self.tail
        prev = tail.prev
        prev.next = node; node.prev = prev
        node.next = tail; tail.prev = node
        self.size += 1

    def put_front(self, node):
        node.nodelist = self
        head = self.head
        next = head.next
        head.next = node; node.prev = head
        node.next = next; next.prev = node
        self.size += 1

    def get_front(self):
        return self.head.next

    def get_back(self):
        return self.tail.prev

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self.size -= 1


def remove_nodelist(nodelist):
    prev = nodelist.prev
    next = nodelist.next
    prev.next = next
    next.prev = prev


def insert_nodelist(nodelist, target_nodelist):
    prev = nodelist.prev
    prev.next = target_nodelist; target_nodelist.prev = prev
    target_nodelist.next = nodelist; nodelist.prev = target_nodelist

def get_front_nodelist(nodelist_head):
    return nodelist_head.next


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.used = 0
        self.map = {}
        self.nodelist_head = NodeList(-1)
        self.nodelist_tail = NodeList(float('inf'))
        self.nodelist_head.next = self.nodelist_tail; self.nodelist_tail.prev = self.nodelist_head

    def get(self, key: int) -> int:
        if self.cap == 0: return -1
        if self.map.get(key, None) == None:
            return -1
        else:
            node = self.map[key]
            nodelist = node.nodelist
            next_nodelist = nodelist.next
            nodelist.remove(node)
            node.freq += 1
            if nodelist.size == 0:
                remove_nodelist(nodelist)
            if node.freq == next_nodelist.freq:
                next_nodelist.put_back(node)
            else:
                new_nodelist = NodeList(node.freq); new_nodelist.put_front(node)
                insert_nodelist(next_nodelist, new_nodelist)
            return node.val


    def put(self, key: int, value: int) -> None:
        if self.cap == 0: return
        if self.map.get(key, None) == None:
            new_node = Node(val=value, key=key, freq=1)
            self.map[key] = new_node
            if self.used < self.cap:
                self.used += 1
            else:
                front_nodelist = get_front_nodelist(self.nodelist_head)
                front_node = front_nodelist.get_front()
                self.map.pop(front_node.key)
                front_nodelist.remove(front_node)
                if front_nodelist.size == 0:
                    remove_nodelist(front_nodelist)

            front_nodelist = get_front_nodelist(self.nodelist_head)
            if front_nodelist.freq == new_node.freq:
                front_nodelist.put_back(new_node)
            else:
                new_nodelist = NodeList(1); new_nodelist.put_front(new_node)
                insert_nodelist(front_nodelist, new_nodelist)

        else:
            node = self.map[key]
            nodelist = node.nodelist
            next_nodelist = nodelist.next
            nodelist.remove(node)
            node.freq += 1; node.val = value
            if nodelist.size == 0:
                remove_nodelist(nodelist)
            if node.freq == next_nodelist.freq:
                next_nodelist.put_back(node)
            else:
                new_nodelist = NodeList(node.freq); new_nodelist.put_front(node)
                insert_nodelist(next_nodelist, new_nodelist)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
