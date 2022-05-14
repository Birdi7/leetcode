from typing import List, Counter
from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count_by_vertex = defaultdict(int)
        for edge in edges:
            count_by_vertex[edge[0]] += 1
            count_by_vertex[edge[1]] += 1
            
            
        return max(count_by_vertex, key=count_by_vertex.get)
    
            


if __name__ == '__main__':
    test_cases = [
        (
            [[1, 2], [2, 3], [4, 2]],
            2
        ),
        (
            [[1, 2], [5, 1], [1, 3], [1, 4]],
            1
        )
    ]
    
    for case in test_cases:
        assert Solution().findCenter(case[0]) == case[1]