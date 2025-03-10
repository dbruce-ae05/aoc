import json
from collections.abc import Iterable


def walk(iterable: Iterable, includetype: type = int, excludestr: str = None) -> list:
    result: list = list()

    if isinstance(iterable, dict):
        if excludestr is not None:
            if excludestr in iterable.keys() or excludestr in iterable.values():
                return []

        for key, value in iterable.items():
            if isinstance(key, Iterable):
                result.extend(walk(key, includetype=includetype, excludestr=excludestr))
            else:
                result.append(key)

            if isinstance(value, Iterable):
                result.extend(
                    walk(value, includetype=includetype, excludestr=excludestr)
                )
            else:
                if isinstance(value, includetype):
                    result.append(value)

    else:
        for iter in iterable:
            if isinstance(iter, Iterable) and not isinstance(iter, str):
                result.extend(
                    walk(iter, includetype=includetype, excludestr=excludestr)
                )
            else:
                if isinstance(iter, includetype):
                    result.append(iter)

    return result


if __name__ == "__main__":
    path = "puzzle_day12.txt"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    results = walk(data)
    results_no_red = walk(data, excludestr="red")

    print(f"The sum of the numbers in data is {sum(results)}")
    print(f"The sum of the numbers in data, without 'red' is {sum(results_no_red)}")
