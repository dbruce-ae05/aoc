from itertools import permutations
from pathlib import Path


def pairs(sequence):
    iterable = iter(sequence)
    prev = next(iterable)
    for item in iterable:
        yield prev, item
        prev = item


def get_routes(distances: list) -> dict:
    locations = set()
    dists = dict()

    for line in distances:
        line = line.replace("to", ",").replace("=", ",").replace(" ", "")
        line = line.split(",")
        locations.add(line[0])
        locations.add(line[1])

        dists[f"{line[0]} -> {line[1]}"] = int(line[2])
        dists[f"{line[1]} -> {line[0]}"] = int(line[2])

    routes = list(permutations(locations, len(locations)))

    result = dict()
    for route in routes:
        key = " -> ".join(route)

        dist = 0
        for start, end in pairs(route):
            dist += dists[f"{start} -> {end}"]

        # print(key, ' = ', dist)

        result[key] = dist

    return result


if __name__ == "__main__":
    path = Path("puzzle_day9.txt")

    with open(path, "r") as f:
        lines = f.read().split("\n")

    lines = lines[:-1]

    routes = get_routes(lines)
    min_route = min(routes.items(), key=lambda x: x[1])
    max_route = max(routes.items(), key=lambda x: x[1])

    print(f"The minimum route is {min_route[0]} -> {min_route[1]}")
    print(f"The maximum route is {max_route[0]} -> {max_route[1]}")
