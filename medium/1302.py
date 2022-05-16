import random
from queue import Queue
from typing import List, Optional
from collections import defaultdict

mrandom = random.Random(1)

queue = Queue()



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = []
        self.by_height = defaultdict(list)
        
    def iterate(self, root, height: int):
        self.by_height[height].append(root)
        if root.left:
            self.iterate(root.left, height+1)
        if root.right:
            self.iterate(root.right, height+1)
            
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.iterate(root, height=0)
        return sum([item.val for item in self.by_height[max(self.by_height.keys())]])
        
        