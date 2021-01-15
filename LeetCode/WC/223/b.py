# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n = 1
        tmp = head
        while tmp.next != None:
            tmp = tmp.next
            n += 1

        k_ = n-k+1
        if k > k_:
            tmp = k
            k = k_
            k_ = tmp

        if n == 1 or k == k_:
            head
        elif n == 2:
            h = head
            h2 = h.next

            h.next = None
            h2.next = h
            head = h2
        elif k == 1 or k == n:
            h = head
            h2 = h.next
            e = head
            e2 = head
            for i in range(n-1):
                e2 = e
                e = e.next

            h.next = None
            e2.next = h
            e.next = h2
            head = e
        else:
            if k_-k==1:
                ll = head
                l = head
                for i in range(k-1):
                    ll = l
                    l = l.next
                r = l.next
                rr = r.next

                ll.next = r
                l.next = rr
                r.next = l
            else:
                llNode = head
                lNode = head
                lrNode = head
                rNode = head
                for i in range(k-1):
                    llNode = lNode
                    lNode = lNode.next
                for i in range(n-k):
                    lrNode = rNode
                    rNode = rNode.next
                rlNode = lNode.next
                rrNode = rNode.next

                lNode.next = rrNode
                rNode.next = rlNode
                llNode.next = rNode
                lrNode.next = lNode

        return head
