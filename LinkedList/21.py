# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode()
        root = l3
        
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                tmp = ListNode(l1.val)
                l3.next = tmp
                
                l1 = l1.next
            else:
                tmp = ListNode(l2.val)
                l3.next = tmp
                
                l2 = l2.next
            
            l3 = l3.next
            
        if l1 != None:
            l3.next = l1
        elif l2 != None:
            l3.next = l2
        
        return root.next