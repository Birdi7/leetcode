import random
from queue import Queue
from typing import List
from collections import defaultdict

mrandom = random.Random(1)

queue = Queue()


class Solution:
    def __init__(self):
        self.result = []
        
    def bfs(self, current: int, visited: dict, *, vertex_to_neighbours: dict):
        if visited.get(current, False):
            return []
        assert current not in visited

        visited[current] = True
        for neighbour in vertex_to_neighbours[current]:
            self.result.append(neighbour)
            if not visited.get(neighbour, False):
                queue.put(neighbour)

        while not queue.empty():
            next_vertex = queue.get()
            queue.task_done()

            self.bfs(
                next_vertex,
                visited,
                vertex_to_neighbours=vertex_to_neighbours,
            )

    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        vertex_to_neighbours = defaultdict(list)
        for edge in edges:
            vertex_to_neighbours[edge[0]].append(edge[1])
            vertex_to_neighbours[edge[1]].append(edge[0])

        if source == destination:
            return True

        visited = {}
        self.bfs(
            current=source, visited=visited, vertex_to_neighbours=vertex_to_neighbours
        )

        return destination in self.result



if __name__ == "__main__":
    result = Solution().validPath(
        10,
        [
            [2, 9],
            [7, 8],
            [5, 9],
            [7, 2],
            [3, 8],
            [2, 8],
            [1, 6],
            [3, 0],
            [7, 0],
            [8, 5],
        ],
        1,
        0,
    )
    print(result)
