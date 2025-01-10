# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse_(start, end):
            prev, curr = None, start
            while (curr != end):
                nn = curr.next
                curr.next = prev
                prev = curr
                curr = nn
            return prev


        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next


        dummynode = ListNode(0)
        dummynode.next = head
        prev = dummynode

        while count >=k:

            start = prev.next
            end = start

            for _ in range(k):
                end = end.next
            
            reversed_list = reverse_(start, end)
            prev.next = reversed_list
            start.next = end
            prev = start

            count -= k

        return dummynode.next

            