from unittest import mock
from utils.intcode_computer import Instruction, Opcode, IntcodeComputer, Parameter


def test_instruction():
    instruction = IntcodeComputer.build_instruction([1, 9, 10, 3])
    assert instruction.opcode == Opcode.ADD
    assert instruction.first == Parameter(0, 9)
    assert instruction.second == Parameter(0, 10)
    assert instruction.result == Parameter(0, 3)


def test_halt_instruction():
    instruction = IntcodeComputer.build_instruction([99, None, None, None])
    assert instruction


def test_create_intcodecomputer():
    values = [int(value) for value in "1,9,10,3,2,3,11,0,99,30,40,50".split(",")]
    computer = IntcodeComputer(values=values)
    first_instruction = computer.current_instruction()
    assert first_instruction == Instruction(
        1, Parameter(0, 9), Parameter(0, 10), Parameter(0, 3)
    )


def test_advance_intcodecomputer():
    values = [int(value) for value in "1,9,10,3,2,3,11,0,99,30,40,50".split(",")]
    computer = IntcodeComputer(values=values)
    next_instruction = computer.execute_current_instruction()
    assert next_instruction == Instruction(
        2, Parameter(0, 3), Parameter(0, 11), Parameter(0, 0)
    )
    assert computer.instruction_pointer == 4


def test_execute_current_instruction():
    values = [int(value) for value in "1,9,10,3,2,3,11,0,99,30,40,50".split(",")]
    computer = IntcodeComputer(values=values)
    next_instruction = computer.execute_current_instruction()
    assert computer.memory == [
        int(value) for value in "1,9,10,70,2,3,11,0,99,30,40,50".split(",")
    ]
    assert next_instruction == Instruction(
        2, Parameter(0, 3), Parameter(0, 11), Parameter(0, 0)
    )


def test_execute_example1():
    start_values_str = "1,9,10,3,2,3,11,0,99,30,40,50"
    end_values_str = "3500,9,10,70,2,3,11,0,99,30,40,50"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    computer.execute()
    assert computer.memory == [int(value) for value in end_values_str.split(",")]


def test_execute_example2():
    start_values_str = "1,0,0,0,99"
    end_values_str = "2,0,0,0,99"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    computer.execute()
    assert computer.memory == [int(value) for value in end_values_str.split(",")]


def test_execute_example3():
    start_values_str = "2,3,0,3,99"
    end_values_str = "2,3,0,6,99"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    computer.execute()
    assert computer.memory == [int(value) for value in end_values_str.split(",")]


def test_execute_example4():
    start_values_str = "2,4,4,5,99,0"
    end_values_str = "2,4,4,5,99,9801"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    computer.execute()
    assert computer.memory == [int(value) for value in end_values_str.split(",")]


def test_execute_example5():
    start_values_str = "1,1,1,4,99,5,6,0,99"
    end_values_str = "30,1,1,4,2,5,6,0,99"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    computer.execute()
    assert computer.memory == [int(value) for value in end_values_str.split(",")]


def test_parse():
    assert Instruction.parse(1002) == (2, 0, 1, 0)


def test_execute_day05_example1():
    start_values_str = "3,0,4,0,99"
    end_values_str = "1,0,4,0,99"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    with mock.patch("builtins.input", return_value="1"):
        computer.execute()
        assert computer.memory == [int(value) for value in end_values_str.split(",")]


def test_execute_day05_example2():
    start_values_str = "1002,4,3,4,33"
    end_values_str = "1002,4,3,4,99"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    computer.execute()
    assert computer.memory == [int(value) for value in end_values_str.split(",")]


def test_execute_day05_example3():
    start_values_str = "1101,100,-1,4,0"
    end_values_str = "1101,100,-1,4,99"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    computer.execute()
    assert computer.memory == [int(value) for value in end_values_str.split(",")]


@mock.patch("builtins.print")
def test_execute_day05_part2_example1_not8(mock_print):
    start_values_str = "3,9,8,9,10,9,4,9,99,-1,8"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    with mock.patch("builtins.input", return_value="1"):
        computer.execute()

    mock_print.assert_called_with("Output 0")


@mock.patch("builtins.print")
def test_execute_day05_part2_example1_8(mock_print):
    start_values_str = "3,9,8,9,10,9,4,9,99,-1,8"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    with mock.patch("builtins.input", return_value="8"):
        computer.execute()

    mock_print.assert_called_with("Output 1")


@mock.patch("builtins.print")
def test_execute_day05_part2_example2_less8(mock_print):
    start_values_str = "3,9,7,9,10,9,4,9,99,-1,8"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    with mock.patch("builtins.input", return_value="1"):
        computer.execute()

    mock_print.assert_called_with("Output 1")


@mock.patch("builtins.print")
def test_execute_day05_part2_example2_greater8(mock_print):
    start_values_str = "3,9,7,9,10,9,4,9,99,-1,8"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    with mock.patch("builtins.input", return_value="9"):
        computer.execute()

    mock_print.assert_called_with("Output 0")


@mock.patch("builtins.print")
def test_execute_day05_part2_example3_not8(mock_print):
    start_values_str = "3,3,1108,-1,8,3,4,3,99"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    with mock.patch("builtins.input", return_value="1"):
        computer.execute()

    mock_print.assert_called_with("Output 0")


@mock.patch("builtins.print")
def test_execute_day05_part2_example3_greater8(mock_print):
    start_values_str = "3,3,1108,-1,8,3,4,3,99"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    with mock.patch("builtins.input", return_value="8"):
        computer.execute()

    mock_print.assert_called_with("Output 1")


@mock.patch("builtins.print")
def test_execute_day05_part2_example4_less8(mock_print):
    start_values_str = "3,3,1107,-1,8,3,4,3,99"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    with mock.patch("builtins.input", return_value="1"):
        computer.execute()

    mock_print.assert_called_with("Output 1")


@mock.patch("builtins.print")
def test_execute_day05_part2_example4_greater8(mock_print):
    start_values_str = "3,3,1107,-1,8,3,4,3,99"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    with mock.patch("builtins.input", return_value="8"):
        computer.execute()

    mock_print.assert_called_with("Output 0")


@mock.patch("builtins.print")
def test_execute_day05_part2_example5_is0(mock_print):
    start_values_str = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    with mock.patch("builtins.input", return_value="0"):
        computer.execute()

    mock_print.assert_called_with("Output 0")


@mock.patch("builtins.print")
def test_execute_day05_part2_example5_isnot0(mock_print):
    start_values_str = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    with mock.patch("builtins.input", return_value="1"):
        computer.execute()

    mock_print.assert_called_with("Output 1")


@mock.patch("builtins.print")
def test_execute_day05_part2_example6_is0(mock_print):
    start_values_str = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    with mock.patch("builtins.input", return_value="0"):
        computer.execute()

    mock_print.assert_called_with("Output 0")


@mock.patch("builtins.print")
def test_execute_day05_part2_example6_isnot0(mock_print):
    start_values_str = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    with mock.patch("builtins.input", return_value="1"):
        computer.execute()

    mock_print.assert_called_with("Output 1")


# The above example program uses an input instruction to ask for a single number.
# The program will then output 999 if the input value is below 8,
# output 1000 if the input value is equal to 8,
# or output 1001 if the input value is greater than 8.
@mock.patch("builtins.print")
def test_execute_day05_part2_example7_below0(mock_print):
    start_values_str = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    with mock.patch("builtins.input", return_value="1"):
        computer.execute()

    mock_print.assert_called_with("Output 999")


@mock.patch("builtins.print")
def test_execute_day05_part2_example7_equal0(mock_print):
    start_values_str = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    with mock.patch("builtins.input", return_value="8"):
        computer.execute()

    mock_print.assert_called_with("Output 1000")


@mock.patch("builtins.print")
def test_execute_day05_part2_example7_greater0(mock_print):
    start_values_str = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
    computer = IntcodeComputer(
        values=[int(value) for value in start_values_str.split(",")]
    )
    with mock.patch("builtins.input", return_value="9"):
        computer.execute()

    mock_print.assert_called_with("Output 1001")
