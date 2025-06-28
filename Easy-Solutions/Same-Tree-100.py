# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        res = [[],[]]

        def inorder(root, idx):
            if not root:
                res[idx].append("null")
                return

            res[idx].append(root.val)
            inorder(root.left, idx)
            inorder(root.right, idx)

        inorder(p, 0)
        inorder(q, 1)

        if res[0] == res[1]:
            return True
        return False

#runtime - 0 ms