# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """


        if not root:
            return 0


        def dfs(root, sum):

            if not root:
                return 0
            if root.val == sum:
                return dfs(root.left, sum - root.val) + dfs(root.right, sum - root.val) + 1
            else:
                return dfs(root.left, sum - root.val) + dfs(root.right, sum - root.val)
            

        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)