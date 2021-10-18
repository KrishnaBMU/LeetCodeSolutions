
class Solution:

    def pathSum(self, root, sum):
        if not root:
            return 0
        return self.pathSumRecursive(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathSumRecursive(self, root, sum):
        if not root:
            return 0

        return (1 if root.val == sum else 0) + self.pathSumRecursive(root.left, sum - root.val) + self.pathSumRecursive(root.right, sum - root.val)

