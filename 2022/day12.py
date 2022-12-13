from typing import Dict, List, Set, Tuple

from utils.input_getter import get_input_for_day


class Graph:
    starts: Set[Tuple[int, int]]
    end: Tuple[int, int]
    heights: Dict[Tuple[int, int], int]

    def __init__(self, inputs: List[str], multi_start: bool = False) -> None:
        self.heights = {}
        self.starts = set()
        for i in range(len(inputs)):
            for j in range(len(inputs[i])):
                if inputs[i][j] == "S":
                    self.starts.add((i, j))
                    self.heights[(i, j)] = ord("a")
                elif inputs[i][j] == "E":
                    self.end = (i, j)
                    self.heights[(i, j)] = ord("z")
                else:
                    if multi_start and inputs[i][j] == "a":
                        self.starts.add((i, j))
                    self.heights[(i, j)] = ord(inputs[i][j])

    def _neighbors(self, pos: Tuple[int, int]) -> Set[Tuple[int, int]]:
        i, j = pos
        c = self.heights.get((i, j))
        neighbors = set()

        possible = {(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)}
        for t in possible:
            h = self.heights.get(t, None)
            if h and h - c <= 1:
                neighbors.add(t)

        return neighbors

    def _reverse_neighbors(self, pos: Tuple[int, int]) -> Set[Tuple[int, int]]:
        # which neighbor can get to pos
        i, j = pos
        c = self.heights.get((i, j))
        neighbors = set()

        possible = {(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)}
        for t in possible:
            h = self.heights.get(t, None)
            if h and c - h <= 1:
                neighbors.add(t)

        return neighbors

    def find_shortest_path(self) -> int:
        q = list(self.heights.keys())
        distances = {t: float("inf") for t in self.heights.keys()}
        previous = {t: None for t in self.heights.keys()}
        distances[self.end] = 0

        while len(q) > 0:
            u = min(q, key=lambda x: distances.get(x))
            q.remove(u)

            if u in self.starts:
                return distances[u]

            for n in self._reverse_neighbors(u):
                if n in q:
                    option = distances[u] + 1
                    if option < distances[n]:
                        distances[n] = option
                        previous[n] = u


if __name__ == "__main__":
    input = get_input_for_day()
    g = Graph(input, multi_start=True)
    print(g.find_shortest_path())
