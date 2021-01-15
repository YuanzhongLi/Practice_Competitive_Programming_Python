class DlinkedNode():
  def __init__(self):
    self.key = 0
    self.value = 0
    self.prev = None
    self.next = None

class LRUCache():
  def _add_node(self, node):
    # Always add the new node right after head.
    node.prev = self.head
    node.next = self.head.next

    self.head.next.prev = node
    self.head.next = node


  def _remove_node(self, node):
    # Remove an existing node from the linked list.
    prev = node.prev
    new = node.next

    prev.next = new
    new.prev = prev

  def _move_to_head(self, node):
    # Move certain node in between to the head.
    self._remove_node(node)
    self._add_node(node)

  def _pop_tail(self):
    # pop the current tail.
    target = self.tail.prev
    self._remove_node(target)
    return target

  def __init__(self, capaticty):
    self.cache = {}
    self.size = 0
    self.capaticty = capaticty
    self.head, self.tail = DlinkedNode(), DlinkedNode()
    self.head.next = self.tail
    self.tail.prev = self.head

  def get(self, key):
    node = self.cache.get(key, None)
    if not node:
      return -1

    self._move_to_head(node)

    return node.value

  def put(self, key, value):
    node = self.cache.get(key, None)

    if not node:
      newNode = DlinkedNode()
      newNode.key = key
      newNode.value = value

      self.cache[key] = newNode
      self._add_node(newNode)

      self.size += 1
      if self.size > self.capaticty:
        tail = self._pop_tail()
        del self.cache[tail.key]
        self.size -= 1

    else:
      node.value = value
      self._move_to_head(node)
