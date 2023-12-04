from day02 import Game, Draw

INPUT = \
    ''''
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''


def test_parse_draw():
    d = '3 blue, 4 red'
    draw = Draw.parse(d)
    assert draw.blue == 3
    assert draw.red == 4


def test_parse_game():
    line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    game = Game.parse(line)
    assert game.id == 1
    assert len(game.draws) == 3


def test_parse_game_double_digits():
    line = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    game = Game.parse(line)
    assert game.id == 3
    assert game.draws == [Draw(6, 20, 8), Draw(5, 4, 13), Draw(0, 1, 5)]
