def get_mid_node(head):
    slow = head
    fast = head
    cnt = 0
    N = None
    while True:
        if fast.next == None:
            N = cnt*2+1
            return slow, N
        elif fast.next.next == None:
            N = (cnt+1)*2
            return slow, N
        else:
            cnt+=1
            slow = slow.next
            fast = fast.next.next

def reverse(start_node):
        prev = start_node
        cur = start_node.next
        if cur == None: return prev
        while True:
            next = cur.next
            cur.next = prev
            prev = cur
            if next == None:
                break
            else:
                cur = next
        return cur	  # 7->6->5

class Solution:
    def reorderList(self, head: ListNode) -> None:
        mid, N = get_mid_node(head)
        if N <= 2: return head
        head2 = reverse(mid.next)
        cur1 = head.next
        cur2 = head2
        cur = head
        for i in range(1,N):
            if i%2 == 0:
                cur.next = cur1
                cur = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur = cur2
                cur2 = cur2.next
        cur.next = None
