# import random
# from queue import Queue
# from typing import List
# from collections import defaultdict
# 
# mrandom = random.Random(1)
# 
# queue = Queue()
# 
# 
# class Solution:
#     def __init__(self):
#         self.result = []
#         self.visited = defaultdict(int)
#         self.count = defaultdict(int)
#         
#     def dfs(
#         self, current: int, *, vertex_to_neighbours: dict, max_n: int
#     ):
#         visited = self.visited
# 
#         if visited[current] == self.count[current]/2:
#             is_ok = True
#             for k, v in visited.items():
#                 if v != self.count:
#                     is_ok = False
#             return is_ok
# 
#         visited[current] += 1
#         for neighbour in vertex_to_neighbours[current]:
#             if visited.get(neighbour, False):
#                 continue
# 
#             dfs_result = self.dfs(
#                 neighbour,
#                 vertex_to_neighbours=vertex_to_neighbours,
#                 max_n=max_n,
#             )
#             if dfs_result:
#                 self.result.append(current)
#                 return True
# 
#         return False
# 
#     def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
#         vertex_to_neighbours = defaultdict(list)
#         max_n = None
#         min_n = None
#         for edge in pairs:
#             vertex_to_neighbours[edge[0]].append(edge[1])
#             vertex_to_neighbours[edge[1]].append(edge[0])
#             self.count[edge[0]] += 1
#             self.count[edge[1]] += 1
#             max_n = (
#                 max(max_n, edge[0], edge[1])
#                 if max_n is not None
#                 else max(edge[0], edge[1])
#             )
#             min_n = (
#                 min(max_n, edge[0], edge[1])
#                 if max_n is not None
#                 else min(edge[0], edge[1])
#             )
#         
#         
#         self.dfs(
#             current=min_n,
#             vertex_to_neighbours=vertex_to_neighbours,
#             max_n=max_n,
#         )
# 
#         return self.result
# 
# 
# if __name__ == "__main__":
#     result = Solution().validArrangement([[5, 1], [4, 5], [11, 9], [9, 4]])
#     print(result)
