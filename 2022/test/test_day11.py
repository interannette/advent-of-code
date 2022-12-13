from day11 import Monkey, MonkeyBusiness


def test_build_monkey():
    inputs = [
        "Starting items: 79, 98",
        "Operation: new = old * 19",
        "Test: divisible by 23",
        "If true: throw to monkey 2",
        "If false: throw to monkey 3",
    ]

    m = Monkey(inputs)

    assert m.items == [79, 98]
    assert m.operation(2) == 38
    assert m.operation(0) == 0
    assert m.test(46) == 2
    assert m.test(47) == 3


def test_monkey_business_init():
    inputs = [
        "Monkey 0:",
        "  Starting items: 79, 98",
        "  Operation: new = old * 19",
        "  Test: divisible by 23",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 3",
        "",
        "Monkey 1:",
        "  Starting items: 54, 65, 75, 74",
        "  Operation: new = old + 6",
        "  Test: divisible by 19",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 0",
        "",
        "Monkey 2:",
        "  Starting items: 79, 60, 97",
        "  Operation: new = old * old",
        "  Test: divisible by 13",
        "    If true: throw to monkey 1",
        "    If false: throw to monkey 3",
        "",
        "Monkey 3:",
        "  Starting items: 74",
        "  Operation: new = old + 3",
        "  Test: divisible by 17",
        "    If true: throw to monkey 0",
        "    If false: throw to monkey 1",
    ]

    monkey_business = MonkeyBusiness(inputs)
    assert len(monkey_business.monkeys) == 4


def test_monkey_business_run():
    inputs = [
        "Monkey 0:",
        "  Starting items: 79, 98",
        "  Operation: new = old * 19",
        "  Test: divisible by 23",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 3",
        "",
        "Monkey 1:",
        "  Starting items: 54, 65, 75, 74",
        "  Operation: new = old + 6",
        "  Test: divisible by 19",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 0",
        "",
        "Monkey 2:",
        "  Starting items: 79, 60, 97",
        "  Operation: new = old * old",
        "  Test: divisible by 13",
        "    If true: throw to monkey 1",
        "    If false: throw to monkey 3",
        "",
        "Monkey 3:",
        "  Starting items: 74",
        "  Operation: new = old + 3",
        "  Test: divisible by 17",
        "    If true: throw to monkey 0",
        "    If false: throw to monkey 1",
    ]

    monkey_business = MonkeyBusiness(inputs)
    monkey_business.execute_round()

    assert monkey_business.round == 1
    assert monkey_business.monkeys[0].items == [20, 23, 27, 26]
    assert monkey_business.monkeys[1].items == [2080, 25, 167, 207, 401, 1046]

    monkey_business.execute_round()

    assert monkey_business.round == 2
    assert monkey_business.monkeys[0].items == [695, 10, 71, 135, 350]
    assert monkey_business.monkeys[1].items == [43, 49, 58, 55, 362]

    monkey_business.execute_round()

    assert monkey_business.round == 3
    assert monkey_business.monkeys[0].items == [16, 18, 21, 20, 122]
    assert monkey_business.monkeys[1].items == [1468, 22, 150, 286, 739]

    monkey_business.execute_round()

    assert monkey_business.round == 4
    assert monkey_business.monkeys[0].items == [491, 9, 52, 97, 248, 34]
    assert monkey_business.monkeys[1].items == [39, 45, 43, 258]

    monkey_business.execute_round()

    assert monkey_business.round == 5
    assert monkey_business.monkeys[0].items == [15, 17, 16, 88, 1037]
    assert monkey_business.monkeys[1].items == [20, 110, 205, 524, 72]

    monkey_business.execute_round()

    assert monkey_business.round == 6
    assert monkey_business.monkeys[0].items == [8, 70, 176, 26, 34]
    assert monkey_business.monkeys[1].items == [481, 32, 36, 186, 2190]

    monkey_business.execute_round()

    assert monkey_business.round == 7
    assert monkey_business.monkeys[0].items == [162, 12, 14, 64, 732, 17]
    assert monkey_business.monkeys[1].items == [148, 372, 55, 72]

    monkey_business.execute_round()

    assert monkey_business.round == 8
    assert monkey_business.monkeys[0].items == [51, 126, 20, 26, 136]
    assert monkey_business.monkeys[1].items == [343, 26, 30, 1546, 36]

    monkey_business.execute_round()

    assert monkey_business.round == 9
    assert monkey_business.monkeys[0].items == [116, 10, 12, 517, 14]
    assert monkey_business.monkeys[1].items == [108, 267, 43, 55, 288]

    monkey_business.execute_round()

    assert monkey_business.round == 10
    assert monkey_business.monkeys[0].items == [91, 16, 20, 98]
    assert monkey_business.monkeys[1].items == [481, 245, 22, 26, 1092, 30]

    monkey_business.execute_round()
    monkey_business.execute_round()
    monkey_business.execute_round()
    monkey_business.execute_round()
    monkey_business.execute_round()

    assert monkey_business.round == 15
    assert monkey_business.monkeys[0].items == [83, 44, 8, 184, 9, 20, 26, 102]
    assert monkey_business.monkeys[1].items == [110, 36]

    monkey_business.execute_round()
    monkey_business.execute_round()
    monkey_business.execute_round()
    monkey_business.execute_round()
    monkey_business.execute_round()

    assert monkey_business.round == 20
    assert monkey_business.monkeys[0].items == [10, 12, 14, 26, 34]
    assert monkey_business.monkeys[1].items == [245, 93, 53, 199, 115]

    assert monkey_business.compute_level() == 10605


def test_second_star_example():
    inputs = [
        "Monkey 0:",
        "  Starting items: 79, 98",
        "  Operation: new = old * 19",
        "  Test: divisible by 23",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 3",
        "",
        "Monkey 1:",
        "  Starting items: 54, 65, 75, 74",
        "  Operation: new = old + 6",
        "  Test: divisible by 19",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 0",
        "",
        "Monkey 2:",
        "  Starting items: 79, 60, 97",
        "  Operation: new = old * old",
        "  Test: divisible by 13",
        "    If true: throw to monkey 1",
        "    If false: throw to monkey 3",
        "",
        "Monkey 3:",
        "  Starting items: 74",
        "  Operation: new = old + 3",
        "  Test: divisible by 17",
        "    If true: throw to monkey 0",
        "    If false: throw to monkey 1",
    ]

    monkey_business = MonkeyBusiness(
        inputs, relief_multiplier=None, big_business_monkeys=True
    )
    monkey_business.execute_round()

    assert monkey_business.monkeys[0].total_inspected == 2
    assert monkey_business.monkeys[1].total_inspected == 4
    assert monkey_business.monkeys[2].total_inspected == 3
    assert monkey_business.monkeys[3].total_inspected == 6

    for i in range(19):
        monkey_business.execute_round()

    assert monkey_business.round == 20
    assert monkey_business.monkeys[0].total_inspected == 99
    assert monkey_business.monkeys[1].total_inspected == 97
    assert monkey_business.monkeys[2].total_inspected == 8
    assert monkey_business.monkeys[3].total_inspected == 103

    for i in range(980):
        monkey_business.execute_round()

    assert monkey_business.round == 1000
    assert monkey_business.monkeys[0].total_inspected == 5204
    assert monkey_business.monkeys[1].total_inspected == 4792
    assert monkey_business.monkeys[2].total_inspected == 199
    assert monkey_business.monkeys[3].total_inspected == 5192

    for i in range(1000):
        monkey_business.execute_round()

    assert monkey_business.round == 2000
    assert monkey_business.monkeys[0].total_inspected == 10419
    assert monkey_business.monkeys[1].total_inspected == 9577
    assert monkey_business.monkeys[2].total_inspected == 392
    assert monkey_business.monkeys[3].total_inspected == 10391

    for i in range(8000):
        monkey_business.execute_round()

    assert monkey_business.round == 10000
    assert monkey_business.monkeys[0].total_inspected == 52166
    assert monkey_business.monkeys[1].total_inspected == 47830
    assert monkey_business.monkeys[2].total_inspected == 1938
    assert monkey_business.monkeys[3].total_inspected == 52013
