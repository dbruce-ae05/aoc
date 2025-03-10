from pathlib import Path

import pytest

from day6 import show_grid
from day13 import arrangement_happiness, get_possible_arrangements, parse_info
from day14 import calculate_race_points, parse_reindeer, race_reindeer
from day15 import optimize_recipe, parse_ingredients, score_recipe
from day17 import get_combinations, get_valid_combinations, is_total_liters
from day18 import get_neighbors, next_grid, read_grid
from day19 import calibrate, make_molecule
from day20 import factor, house_presents
from day21 import Player, winner


def test_parse_info():
    path = Path("day13_tst_data.txt")

    truth_dict = {
        "Alice": {"Bob": 54, "Carol": -79, "David": -2},
        "Bob": {"Alice": 83, "Carol": -7, "David": -63},
        "Carol": {"Alice": -62, "Bob": 60, "David": 55},
        "David": {"Alice": 46, "Bob": -7, "Carol": 41},
    }

    assert parse_info(path) == truth_dict


def test_possible_arrangements():
    pass
    # path = Path("day13_tst_data.txt")
    # data = parse_info(path)
    # print()
    # print(list(get_possible_arrangements(data)))


def test_arrangement_happiness():
    path = Path("day13_tst_data.txt")
    data = parse_info(path)

    assert (
        arrangement_happiness(("David", "Alice", "Bob", "Carol", "David"), data) == 330
    )


def test_parse_data():
    path = Path("day14_tst_data.txt")

    data = parse_reindeer(path)

    race = race_reindeer(data, 1000)

    assert sum(race["Comet"]["schedule"]) == 1120
    assert sum(race["Dancer"]["schedule"]) == 1056

    # print()
    # print("Comet,Dancer")
    # comet_schedule = race["Comet"]["schedule"]
    # dancer_schedule = race["Dancer"]["schedule"]
    # for i in range(len(comet_schedule)):
    #     print(f"{comet_schedule[i]},{dancer_schedule[i]}")

    race = calculate_race_points(data, 1000)
    assert sum(race["Comet"]["points"]) == 312
    assert sum(race["Dancer"]["points"]) == 689


def test_parse_ingredients():
    path = Path("day15_tst_data.txt")

    truth_dict = {
        "Butterscotch": {
            "capacity": -1,
            "durability": -2,
            "flavor": 6,
            "texture": 3,
            "calories": 8,
        },
        "Cinnamon": {
            "capacity": 2,
            "durability": 3,
            "flavor": -2,
            "texture": -1,
            "calories": 3,
        },
    }

    test_dict = parse_ingredients(path)
    # print(test_dict)

    assert test_dict == truth_dict


def test_score_recipe():
    path = Path("day15_tst_data.txt")
    test_dict = parse_ingredients(path)

    assert score_recipe({"Butterscotch": 44, "Cinnamon": 56}, test_dict) == 62842880
    assert (
        score_recipe({"Butterscotch": 40, "Cinnamon": 60}, test_dict, 500) == 57600000
    )


def test_optimize_recipe():
    data = {
        "Butterscotch": {
            "capacity": -1,
            "durability": -2,
            "flavor": 6,
            "texture": 3,
            "calories": 8,
        },
        "Cinnamon": {
            "capacity": 2,
            "durability": 3,
            "flavor": -2,
            "texture": -1,
            "calories": 3,
        },
    }

    result = optimize_recipe(data, 100)
    assert result == "{'Butterscotch': 44, 'Cinnamon': 56} = 62842880"

    result = optimize_recipe(data, 100, 500)
    assert result == "{'Butterscotch': 40, 'Cinnamon': 60} = 57600000"


def test_is_total_liters():
    assert is_total_liters((15, 10), 25)
    assert is_total_liters((20, 5), 25)
    assert is_total_liters((15, 5, 5), 25)


def test_valid_get_combinations():
    valid_combs = [(15, 10), (20, 5), (20, 5), (15, 5, 5)]
    containers = (20, 15, 10, 5, 5)
    test_combs = get_valid_combinations(containers, 25)

    assert len(valid_combs) == len(test_combs)

    for comb in valid_combs:
        assert comb in test_combs


def test_get_neighbors():
    input_str = """
1B5...
234...
......
..123.
..8A4.
..765.
"""

    # print()

    grid = read_grid(input_str=input_str)
    # show_grid(grid)
    neighbors = get_neighbors((0, 1), grid, 6, 6)
    # print(neighbors)
    assert len(neighbors) == 5
    for i in range(1, 6):
        assert str(i) in neighbors

    neighbors = get_neighbors((4, 3), grid, 6, 6)
    # print(neighbors)
    assert len(neighbors) == 8
    for i in range(1, 9):
        assert str(i) in neighbors


def test_read_grid():
    path: list = list()
    path.append("day18_tst_data_0.txt")
    path.append("day18_tst_data_1.txt")
    path.append("day18_tst_data_2.txt")
    path.append("day18_tst_data_3.txt")
    path.append("day18_tst_data_4.txt")

    truth_grids: list = list()
    for input in path:
        truth_grids.append(read_grid(path=input))

    grid = read_grid(path[0])
    for i, truth_grid in enumerate(truth_grids):
        assert grid == truth_grid
        grid = next_grid(grid)


def test_calibrate():
    molecule = "HOH"
    replacements = [("H", "HO"), ("H", "OH"), ("O", "HH")]

    result = calibrate(molecule, replacements)
    assert len(result) == 4
    assert "HOOH" in result
    assert "HOHO" in result
    assert "OHOH" in result
    assert "HOOH" in result
    assert "HHHH" in result

    molecule = "HOHOHO"
    result = calibrate(molecule, replacements)
    assert len(result) == 7

    molecule = "H2O"
    replacements = [("H", "OO")]
    result = calibrate(molecule, replacements)
    assert result == {"OO2O"}


def test_make_molecule():
    molecule = "e"
    replacements = [("e", "H"), ("e", "O"), ("H", "HO"), ("H", "OH"), ("O", "HH")]

    assert make_molecule(molecule, "HOH", replacements) == 3
    assert make_molecule(molecule, "HOHOHO", replacements) == 6


def test_factor():
    assert factor(1) == (1,)
    assert factor(2) == (1, 2)
    assert factor(3) == (1, 3)
    assert factor(4) == (1, 2, 4)
    assert factor(5) == (1, 5)
    assert factor(6) == (1, 2, 3, 6)
    assert factor(7) == (1, 7)
    assert factor(8) == (1, 2, 4, 8)
    assert factor(9) == (1, 3, 9)
    assert factor(10) == (1, 2, 5, 10)
    assert factor(11) == (1, 11)
    assert factor(12) == (1, 2, 3, 4, 6, 12)
    assert factor(13) == (1, 13)


def test_house_presents():
    assert house_presents(1) == 10
    assert house_presents(2) == 30
    assert house_presents(3) == 40
    assert house_presents(4) == 70
    assert house_presents(5) == 60
    assert house_presents(6) == 120
    assert house_presents(7) == 80
    assert house_presents(8) == 150
    assert house_presents(9) == 130


def test_winner():
    player = Player(hit=8, damage=5, armor=5, name="player", cost=0)
    boss = Player(hit=12, damage=7, armor=2, name="boss", cost=0)
    assert winner(player, boss) == player


if __name__ == "__main__":
    pass
