#Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        result = []
        if root is None: return result
        self.levelordertrav([root], 0, result)
        return result

    def levelordertrav(self, rootlist, level, result):
        newlist = []
        value = []
        if len(rootlist) == 0: return
        for x in rootlist:
            value.append(x.val)
            if x.left is not None: newlist.append(x.left)
            if x.right is not None: newlist.append(x.right)
        if level % 2 == 1: value = value[::-1]
        result.append(value)
        self.levelordertrav(newlist, level + 1, result)