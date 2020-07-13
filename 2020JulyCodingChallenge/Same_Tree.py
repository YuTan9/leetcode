# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        def isSameNode(p, q):
            if p != None and q != None:
                if p.val == q.val:
                    return True
                else:
                    return False
            elif p == None and q == None:
                return True
            else:
                return False
            
            
        same = isSameNode(p,q)
        if p != None and q != None:
            if same:
                same = self.isSameTree(p.left, q.left)
                if same:
                    same = self.isSameTree(p.right, q.right)
                else:
                    return False
            else:
                return False
        return same
                
"""
Better Solution:

if p is None and q is None:
    return True
if p is not None and q is not None:
    return (p.val==q.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
return False
        
"""