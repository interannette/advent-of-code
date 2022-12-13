from day12 import Graph


def test_graph_init():
    input = ["Sabqponm", "abcryxxl", "accszExk", "acctuvwj", "abdefghi"]
    g = Graph(input)
    assert g
    assert g.starts == {(0, 0)}
    assert g.end == (2, 5)
    assert g.heights.get((0, 0)) == ord("a")
    assert g.heights.get((2, 5)) == ord("z")
    assert g.heights.get((0, 1)) == ord("a")


def test_shortest_path():
    input = ["Sabqponm", "abcryxxl", "accszExk", "acctuvwj", "abdefghi"]
    g = Graph(input)
    shortest = g.find_shortest_path()
    assert 31 == shortest


def test_shortest_path_two():
    input = ["Sabqponm", "abcryxxl", "accszExk", "acctuvwj", "abdefghi"]
    g = Graph(input, multi_start=True)
    shortest = g.find_shortest_path()
    assert 29 == shortest
