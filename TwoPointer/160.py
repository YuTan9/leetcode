# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Note that the end of two LL are actually sharing the same memory.
(Not different memory but same value)
"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ptrA = headA
        ptrB = headB
        while ptrA != ptrB:
            if ptrA != None:
                ptrA = ptrA.next
            else:
                ptrA = headB
            if ptrB != None:
                ptrB = ptrB.next
            else:
                ptrB = headA
        
        return ptrA