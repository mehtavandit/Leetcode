# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow, fast = head, head.next

        while fast and fast.next: #finding the middle of a list
            slow = slow.next
            fast = fast.next.next


        second = slow.next #breaking the list into two part first half and second half
        slow.next = None
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        


        # nodes = []
        # curr = head
        # while(curr):
        #     nodes.append(curr)
        #     curr = curr.next


        # left = 0 #left right are just the indexes, you need nodes[index]
        # right = len(nodes) - 1 

        # while left < right:
        #     nodes[left].next = nodes[right]
        #     left += 1
        #     if left == right:
        #         break
        #     nodes[right].next = nodes[left]
        #     right -= 1

        # nodes[left].next = None
