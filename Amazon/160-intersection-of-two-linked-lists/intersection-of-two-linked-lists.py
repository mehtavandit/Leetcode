# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # tempA = headA

        # while tempA is not None:
        #     tempB = headB

        #     while tempB is not None:
        #         if tempA == tempB:
        #             return tempA
        #         tempB = tempB.next

        #     tempA = tempA.next

        # return None

        #TC :- O(m * n) and SC :- O(1) need to optimize

        if not headA or not headB:
            return None

        p1, p2 = headA, headB

        while p1!=p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1
