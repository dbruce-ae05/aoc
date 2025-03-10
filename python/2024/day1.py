from collections import Counter
from pathlib import Path


def read_data(path: Path, output: int = 0) -> list:
    a: list = list()
    b: list = list()

    with open(path) as f:
        lines = f.readlines()

    for line in lines:
        items = line.strip().split("   ")

        a.append(int(items[0]))
        b.append(int(items[1]))

    a = sorted(a)
    b = sorted(b)

    if output == 0:
        return zip(a, b)
    if output == 1:
        return a, b


def calculate_distance(ids: list) -> int:
    result: int = 0
    for a, b in ids:
        result += abs(a - b)

    return result


def calculate_similarity(a: list, b: list) -> int:
    result: int = 0

    group: Counter = Counter(b)

    for item in a:
        if item in group.keys():
            result += item * group[item]

    return result


if __name__ == "__main__":
    ids = read_data("day1_puzzle.txt")
    distance = calculate_distance(ids)

    print(f"The distance is: {distance}")

    a, b = read_data("day1_puzzle.txt", 1)
    similarity = calculate_similarity(a, b)

    print(f"The similarity is: {similarity}")
