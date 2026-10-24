class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        q = collections.deque()
        cur_root = root
        q.append(cur_root)
        res = []
        while q:
            cur_level = []
            for i in range(len(q)):
                if not cur_root:
                    break
                cur_root = q.popleft()
                if cur_root.left:
                    q.append(cur_root.left)
                if cur_root.right:
                    q.append(cur_root.right)
                cur_level.append(cur_root.val)
            res.append(cur_level)
        return res
