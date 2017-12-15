import re


def check_condition(registers, register, op, value):
    current = registers.get(register)
    if not current:
        current = 0

    condition_string = str(current) + op + str(value)
    result = eval(condition_string)

    return result


def do_operation(registers, register, action, value):
    current = registers.get(register)

    if not current:
        current = 0

    if action == 'inc':
        current += value
    else:
        current -= value

    registers[register] = current


def process_line(registers, line):

    regex = re.compile("(\w*) (inc|dec) ([\-0-9]*) if (\w*) ([><=!]*) ([\-0-9]*)")

    result = regex.match(line)
    register = result.group(1)
    action = result.group(2)
    action_value = int(result.group(3))
    check_register = result.group(4)
    check_op = result.group(5)
    check_value = int(result.group(6))

    if check_condition(registers, check_register, check_op, check_value):
        do_operation(registers, register, action, action_value)


def process_input(input_string):
    registers = {}
    lines = input_string.split("\n")
    for line in lines:
        process_line(registers, line)

    max_value = 0
    for value in registers.values():
        if value > max_value:
            max_value = value

    return max_value
