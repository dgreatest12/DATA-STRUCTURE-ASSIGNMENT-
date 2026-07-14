# 7_tree.py — Binary Search Tree with BFS and DFS traversals
# Time complexity: insert/search O(log n) avg, BFS/DFS O(n)

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value, keeping BST ordering (left < node < right)."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def bfs(self):
        """Breadth-First Search — visit level by level using a queue."""
        if not self.root:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def dfs_preorder(self, node=None, first_call=True):
        """Pre-order DFS: visit node → left → right."""
        if first_call:
            node = self.root
        if node is None:
            return []
        return ([node.value]
                + self.dfs_preorder(node.left, False)
                + self.dfs_preorder(node.right, False))

    def dfs_inorder(self, node=None, first_call=True):
        """In-order DFS: visit left → node → right (gives sorted order)."""
        if first_call:
            node = self.root
        if node is None:
            return []
        return (self.dfs_inorder(node.left, False)
                + [node.value]
                + self.dfs_inorder(node.right, False))


# ── Demo ─────────────────────────────────────────────────
bst = BinarySearchTree()
values = [50, 30, 70, 20, 40, 60, 80]   # 7 nodes

print("=== Binary Search Tree Demo ===")
print(f"\nInserting values: {values}")
for v in values:
    bst.insert(v)

print(f"""
Tree structure:
         50
        /  \\
      30    70
     / \\   / \\
   20  40 60  80
""")

print(f"BFS (level-order)  : {bst.bfs()}")
print(f"DFS pre-order      : {bst.dfs_preorder()}")
print(f"DFS in-order       : {bst.dfs_inorder()}  ← sorted!")
