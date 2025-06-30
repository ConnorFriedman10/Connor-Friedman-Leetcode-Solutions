class Solution(object):
    def isSymmetric(self, root):
        res = [[],[]]

        p = root.left
        q = root.right

        def inorder(root, idx):
            if not root:
                res[idx].append("null")
                return

            res[idx].append(root.val)
            inorder(root.left, idx)
            inorder(root.right, idx)

        def reverse_inorder(root, idx):
            if not root:
                res[idx].append("null")
                return

            res[idx].append(root.val)
            reverse_inorder(root.right, idx)
            reverse_inorder(root.left, idx)

        inorder(p, 0)
        reverse_inorder(q, 1)

        if res[0] == res[1]:
            return True
        return False

#runtime - 0 ms