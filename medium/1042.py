import random
from queue import Queue
from typing import List
from collections import defaultdict

possible_choices = [1, 2, 3, 4]


mrandom = random.Random(1)


class Solution:
    def bfs(
        self, current: int, visited: dict, *, result: dict, vertex_to_neighbours: dict
    ):
        if visited.get(current, False):
            return
        assert current in result
        assert current not in visited

        visited[current] = True
        queue = Queue()
        for neighbour in vertex_to_neighbours[current]:
            picked = [
                result[current],
                *[
                    result[nn]
                    for nn in vertex_to_neighbours[neighbour] if nn in result
                ],
            ]

            if neighbour not in result:
                result[neighbour] = mrandom.choice(
                    [item for item in possible_choices if item not in picked]
                )
            queue.put(neighbour)

        while not queue.empty():
            next_vertex = queue.get()
            queue.task_done()

            self.bfs(
                next_vertex,
                visited,
                result=result,
                vertex_to_neighbours=vertex_to_neighbours,
            )

    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        vertex_to_neighbours = defaultdict(list)
        for path in paths:
            vertex_to_neighbours[path[0]].append(path[1])
            vertex_to_neighbours[path[1]].append(path[0])

        result = {}
        visited = {}

        while len(visited) != n:
            current = None
            for i in range(1, n + 1):
                if i not in visited:
                    current = i
                    break
            result[current] = mrandom.choice(possible_choices)
            self.bfs(
                current=current,
                visited=visited,
                result=result,
                vertex_to_neighbours=vertex_to_neighbours,
            )

        return [result[i] for i in range(1, n + 1)]


if __name__ == "__main__":

    result = Solution().gardenNoAdj(
        6, [[6, 4], [6, 1], [3, 1], [4, 5], [2, 1], [5, 6], [5, 2]]
    )
    print(result)
