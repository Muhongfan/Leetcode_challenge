
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

import collections
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        Q = collections.deque([root])

        while Q:
            size = len(Q)
            for i in range(size):
                node = Q.popleft()
                if i < size -1:
                    node.next = Q[0]
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        return root

So = Solution()
print(So.connect([1,2,3,4,5,6,7]))
"""
                        queue: 1
            1(popleft)  queue: 2 3
          2(popleft)->  queue: 3 4 5
            3(popleft)  queue: 4 5 6 7
          4(popleft)->  queue: 5 6 7
          5(popleft)->  queue: 6 7
          6(popleft)->  queue: 7
          7(popleft)->  queue:

"""