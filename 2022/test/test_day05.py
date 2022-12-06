from day05 import Move, Dock, run_steps, build_end_str, CrateMover9001


def test_move_parser():
    output = Move.parse("move 10 from 2 to 1")
    assert output == Move(10, 2, 1)


def test_dock_parser_example():
    input = ["    [D]    ", "[N] [C]    ", "[Z] [M] [P]"]
    ouput = Dock.parse(input)
    expected_stacks = {1: ["[N]", "[Z]"], 2: ["[D]", "[C]", "[M]"], 3: ["[P]"]}
    assert ouput == Dock(expected_stacks)


def test_dock_parser_real():
    input = [
        "    [H]         [H]         [V]    ",
        "    [V]         [V] [J]     [F] [F]",
        "    [S] [L]     [M] [B]     [L] [J]",
        "    [C] [N] [B] [W] [D]     [D] [M]",
        "[G] [L] [M] [S] [S] [C]     [T] [V]",
        "[P] [B] [B] [P] [Q] [S] [L] [H] [B]",
        "[N] [J] [D] [V] [C] [Q] [Q] [M] [P]",
        "[R] [T] [T] [R] [G] [W] [F] [W] [L]",
    ]
    output = Dock.parse(input)
    assert output


def test_dock_move_example1():
    input = ["    [D]    ", "[N] [C]    ", "[Z] [M] [P]"]
    output = Dock.parse(input)
    move = Move(1, 2, 1)
    output.apply_move(move)
    expected_stacks = {1: ["[D]", "[N]", "[Z]"], 2: ["[C]", "[M]"], 3: ["[P]"]}
    assert output == Dock(expected_stacks)


def test_dock_move_example2():
    dock = Dock({1: ["[D]", "[N]", "[Z]"], 2: ["[C]", "[M]"], 3: ["[P]"]})
    move = Move(3, 1, 3)
    dock.apply_move(move)
    expected_stacks = {
        1: [],
        2: ["[C]", "[M]"],
        3: ["[Z]", "[N]", "[D]", "[P]"],
    }
    assert dock == Dock(expected_stacks)


def test_run_steps_first():
    input = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]

    end_state = run_steps(input, Dock)
    expected_output = Dock(
        {
            1: ["[C]"],
            2: ["[M]"],
            3: ["[Z]", "[N]", "[D]", "[P]"],
        }
    )
    assert expected_output == end_state


def test_build_end_str():
    end_state = Dock(
        {
            1: ["[C]"],
            2: ["[M]"],
            3: ["[Z]", "[N]", "[D]", "[P]"],
        }
    )
    assert "CMZ" == build_end_str(end_state)


def test_run_steps_second():
    input = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]

    end_state = run_steps(input, CrateMover9001)
    expected_output = CrateMover9001(
        {
            1: ["[M]"],
            2: ["[C]"],
            3: ["[D]", "[N]", "[Z]", "[P]"],
        }
    )
    assert expected_output == end_state
