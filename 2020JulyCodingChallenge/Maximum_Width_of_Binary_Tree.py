# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# My code: (Passes)
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        width = 1
        parents = [root]
        stop = False
        while not stop:
            level = []
            for parent in parents:
                if parent != None:
                    level.append(parent.left)
                    level.append(parent.right)
                if parent == None and level != []:
                    level.append(None)
                    level.append(None)


            left = -1
            right= len(level)

            for i in range(len(level)):
                if level[i] != None:
                    left = i
                    break

            for i in range(len(level) - 1, -1, -1):
                if level[i] != None:
                    right = i
                    break
                    
            if left != -1 and right != len(level):
                if right - left + 1 > width:
                    width = right - left + 1 
            else:
                stop = True

            parents = list(level)

        return width

"""
# Better solution:

class Solution(object):
    def widthOfBinaryTree(self, root):

        if not root:
            return 0

        max_width = 0
        # queue of elements [(node, col_index)]
        queue = deque()
        queue.append((root, 0))
        print(queue)
        while queue:
            level_length = len(queue)
            # level_head_index would be the first index of each level
            _, level_head_index = queue[0]
            # iterate through the current level
            for _ in range(level_length):
                node, col_index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * col_index))
                    # cuz the left child is the 2 * n in its level, where n is its parent's number
                if node.right:
                    queue.append((node.right, 2 * col_index + 1))

            max_width = max(max_width, col_index - level_head_index + 1)
            
        return max_width
"""