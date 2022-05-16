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

    def iterate(self, root, height):
        if not root:
            return
        if len(self.result) <= height:
            self.result.append([])
        
        if root.val is not None:
            self.result[height-1].append(root.val)

        queue = Queue()
        for child in (root.children or []):
            queue.put(child)
        while not queue.empty():
            next_v = queue.get()
            queue.task_done()
            self.iterate(next_v, height + 1)

    def levelOrder(self, root: "Node") -> List[List[int]]:
        self.iterate(root, 1)
        self.result = list(filter(bool, self.result))
        return self.result


if __name__ == "__main__":
    case = Node(
        val=1,
        children=[
            Node(val=10, children=[Node(5), Node(0)]),
            Node(val=3, children=[Node(val=6)]),
        ],
    )

    print(Solution().levelOrder(case))
