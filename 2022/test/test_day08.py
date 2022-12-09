from day08 import Forest, Tree


def test_parse_forest():
    inputs = ["30373", "25512", "65332", "33549", "35390"]
    f = Forest(inputs)
    expected_trees = [
        [
            Tree(3, True, 0),
            Tree(0, True, 0),
            Tree(3, True, 0),
            Tree(7, True, 0),
            Tree(3, True, 0),
        ],
        [
            Tree(2, True, 0),
            Tree(5, False, -1),
            Tree(5, False, -1),
            Tree(1, False, -1),
            Tree(2, True, 0),
        ],
        [
            Tree(6, True, 0),
            Tree(5, False, -1),
            Tree(3, False, -1),
            Tree(3, False, -1),
            Tree(2, True, 0),
        ],
        [
            Tree(3, True, 0),
            Tree(3, False, -1),
            Tree(5, False, -1),
            Tree(4, False, -1),
            Tree(9, True, 0),
        ],
        [
            Tree(3, True, 0),
            Tree(5, True, 0),
            Tree(3, True, 0),
            Tree(9, True, 0),
            Tree(0, True, 0),
        ],
    ]
    assert expected_trees == f.trees


def test_update_visibility():
    inputs = ["30373", "25512", "65332", "33549", "35390"]
    f = Forest(inputs)
    f.update_visibility()
    expected_trees = [
        [
            Tree(3, True, 0),
            Tree(0, True, 0),
            Tree(3, True, 0),
            Tree(7, True, 0),
            Tree(3, True, 0),
        ],
        [
            Tree(2, True, 0),
            Tree(5, True, -1),
            Tree(5, True, -1),
            Tree(1, False, -1),
            Tree(2, True, 0),
        ],
        [
            Tree(6, True, 0),
            Tree(5, True, -1),
            Tree(3, False, -1),
            Tree(3, True, -1),
            Tree(2, True, 0),
        ],
        [
            Tree(3, True, 0),
            Tree(3, False, -1),
            Tree(5, True, -1),
            Tree(4, False, -1),
            Tree(9, True, 0),
        ],
        [
            Tree(3, True, 0),
            Tree(5, True, 0),
            Tree(3, True, 0),
            Tree(9, True, 0),
            Tree(0, True, 0),
        ],
    ]
    assert expected_trees == f.trees
    assert 21 == f.visible_trees


def test_scenic_score():
    inputs = ["30373", "25512", "65332", "33549", "35390"]
    f = Forest(inputs)
    f.compute_scenic_scores()
    assert f.trees[1][2].scenic_score == 4
    assert f.trees[3][2].scenic_score == 8
    assert 8 == f.max_scenic_score
