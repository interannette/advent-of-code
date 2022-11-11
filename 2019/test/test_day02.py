from day02 import Instruction, Opcode, IntcodeComputer


def test_instruction():
    instruction = Instruction(1, 9, 10, 3)
    assert instruction.opcode == Opcode.ADD
    assert instruction.first_arg_pos == 9
    assert instruction.second_arg_pos == 10
    assert instruction.result_pos == 3


def test_halt_instruction():
    instruction = Instruction(99, None, None, None)
    assert instruction


def test_create_intcodecomputer():
    values = [int(value) for value in "1,9,10,3,2,3,11,0,99,30,40,50".split(",")]
    computer = IntcodeComputer(values=values)
    first_instruction = computer.current_instruction()
    assert first_instruction == Instruction(1, 9, 10, 3)


def test_advance_intcodecomputer():
    values = [int(value) for value in "1,9,10,3,2,3,11,0,99,30,40,50".split(",")]
    computer = IntcodeComputer(values=values)
    next_instruction = computer.advance()
    assert next_instruction == Instruction(2, 3, 11, 0)
    assert computer.instruction_pointer == 4


def test_execute_current_instruction():
    values = [int(value) for value in "1,9,10,3,2,3,11,0,99,30,40,50".split(",")]
    computer = IntcodeComputer(values=values)
    next_instruction = computer.execute_current_instruction()
    assert computer.memory == [
        int(value) for value in "1,9,10,70,2,3,11,0,99,30,40,50".split(",")
    ]
    assert next_instruction == Instruction(2, 3, 11, 0)


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
