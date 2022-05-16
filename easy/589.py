import random
from queue import Queue
from typing import List, Optional
from collections import defaultdict

mrandom = random.Random(1)

queue = Queue()


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.result = []
        
    def iterate(self, root):
        if not root:
            return
        if root.val is not None:
            self.result.append(root.val)
        for child in (root.children or []):
            self.iterate(child)
        
    def preorder(self, root: 'Node') -> List[int]:
        self.iterate(root)
        return self.result
    
if __name__ == '__main__':
    case = Node(
        val=1,
        children=[
            Node(val=10,
                 children=[Node(5),
                           Node(0)]),
            Node(val=3,
                 children=[
                     Node(val=6)
                 ]),
        ]
    )
    
    print(Solution().preorder(case))