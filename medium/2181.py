
import random
from queue import Queue
from typing import List, Optional
from collections import defaultdict

mrandom = random.Random(1)

queue = Queue()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def __init__(self):
        self.result: List[ListNode] = []
        self.current_list = []
    
    def reduce(self):
        return ListNode(val=sum(v.val for v in self.current_list))
    
    def clear(self):
        self.current_list = []
        
    def iterate(self, root):
        if not root:
            return
        if root.val == 0:
            if self.current_list:
                if not self.result:
                    self.result.append(self.reduce())
                else:
                    reduced = self.reduce()
                    self.result[-1].next = reduced
                    self.result.append(reduced)
                self.clear()
        else:
            self.current_list.append(root)
        self.iterate(root.next)
        
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        self.iterate(head)
        if not self.result:
            return None
        return self.result[0]
    

def _get_case(values):
    if len(values) == 1:
        return ListNode(val=values[0])
    
    return ListNode(
        val=values[0],
        next=_get_case(values[1:])
    )

if __name__ == '__main__':
    l = [
        0, 1, 0, 3, 0, 2, 2, 0
    ]
    
    case = _get_case(l)
    print(Solution().mergeNodes(case))
    