from itertools import permutations
from pathlib import Path

from day9 import pairs


def parse_info(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    result: dict = dict()

    for line in lines:
        parsed = line.split(" ")

        key = parsed[0]

        if parsed[2] == "gain":
            sign = 1
        if parsed[2] == "lose":
            sign = -1

        if key not in result.keys():
            result[key] = dict()

        result[key][parsed[-1].replace(".", "")] = sign * int(parsed[3])

    return result


def get_possible_arrangements(data: dict) -> list[tuple]:
    original = permutations(data.keys(), r=len(data.keys()))
    results: list = list()
    for result in original:
        results.append((*result, result[0]))

    return results


def arrangement_happiness(arrangement: tuple, data: dict) -> int:
    result: int = 0
    for first, second in pairs(arrangement):
        result += data[first][second]
        result += data[second][first]
        # print(f"{first=} {second=} {data[first][second] + data[second][first]}")

    return result


if __name__ == "__main__":
    path = "puzzle_day13.txt"

    data = parse_info(path)
    arrangements = get_possible_arrangements(data)

    result: dict = dict()
    for arrangement in arrangements:
        result[arrangement] = arrangement_happiness(arrangement, data)

    print(f"The optimal arrangment is {max(result)}")
    print(f"The optional happiness is {max(result.values())}")

    data2 = parse_info(path)
    temp: dict = dict()
    for key in data2.keys():
        temp[key] = 0
        data2[key]["Me"] = 0

    data2["Me"] = temp
    arrangements2 = get_possible_arrangements(data2)

    result: dict = dict()
    for arrangement in arrangements2:
        result[arrangement] = arrangement_happiness(arrangement, data2)

    print(f"The optimal arrangment with me is {max(result)}")
    print(f"The optional happiness with me is {max(result.values())}")
