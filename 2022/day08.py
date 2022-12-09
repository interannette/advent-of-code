from dataclasses import dataclass
from typing import List
from utils.input_getter import get_input_for_day


@dataclass
class Tree:
    height: int
    visible: bool
    scenic_score: int


class Forest:
    # row, column
    trees: List[List[Tree]]
    visible_trees: int
    max_scenic_score: int

    def __init__(self, inputs: List[str]):
        self.trees = []
        self.visible_trees = 0
        for i in range(len(inputs)):
            input = inputs[i]
            row = []
            for j in range(len(input)):
                visible = False
                if i == 0 or i == len(inputs) - 1:
                    visible = True
                elif j == 0 or j == len(input) - 1:
                    visible = True
                row.append(Tree(int(input[j]), visible, 0 if visible else -1))
                if visible:
                    self.visible_trees += 1
            self.trees.append(row)

    def update_visibility(self):
        for i in range(1, len(self.trees) - 1):
            row = self.trees[i]
            for j in range(1, len(row) - 1):
                tree = row[j]
                if all([(t.height < tree.height) for t in row[:j]]):
                    visible = True
                elif all([(t.height < tree.height) for t in row[j + 1 :]]):
                    visible = True
                elif all(
                    [(self.trees[t][j].height < tree.height) for t in range(0, i)]
                ):
                    visible = True
                elif all(
                    [
                        (self.trees[t][j].height < tree.height)
                        for t in range(i + 1, len(self.trees))
                    ]
                ):
                    visible = True
                else:
                    visible = False
                tree.visible = visible
                if visible:
                    self.visible_trees += 1

    def compute_scenic_scores(self):
        self.max_scenic_score = 0
        for i in range(1, len(self.trees) - 1):
            row = self.trees[i]
            for j in range(1, len(row) - 1):
                score = self._compute_specific_scenic_score(i, j)
                if score > self.max_scenic_score:
                    self.max_scenic_score = score

    def _compute_specific_scenic_score(self, i: int, j: int) -> int:

        if i == 0 or j == 0 or i == len(self.trees) or j == len(self.trees[0]):
            self.trees[i][j].height = 0
            return 0

        height = self.trees[i][j].height

        up_score = 0
        # [i-x][j]
        # 0 = i - x -> x = i
        for x in range(1, i + 1):
            up_score = x
            if self.trees[i - x][j].height >= height:
                break

        down_score = 0
        # [i+x][j]
        # len(self.trees) = i + x -> len(self.trees) - i = x
        for x in range(1, len(self.trees) - i):
            down_score = x
            if self.trees[i + x][j].height >= height:
                break

        left_score = 0
        # [i][j-x]
        # j-x = 0 -> j = x
        for x in range(1, j + 1):
            left_score = x
            if self.trees[i][j - x].height >= height:
                break

        right_score = 0
        # [i][j+x]
        # j+x = len(self.trees[i]) -> x = len(self.trees[i]) - j
        for x in range(1, len(self.trees[i]) - j):
            right_score = x
            if self.trees[i][j + x].height >= height:
                break

        score = up_score * down_score * left_score * right_score
        self.trees[i][j].scenic_score = score
        return score


def first_star():
    input = get_input_for_day()
    f = Forest(input)
    f.update_visibility()
    print(f.visible_trees)


def second_star():
    input = get_input_for_day()
    f = Forest(input)
    f.compute_scenic_scores()
    print(f.max_scenic_score)


if __name__ == "__main__":
    second_star()
