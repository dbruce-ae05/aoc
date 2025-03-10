from itertools import combinations, permutations


def is_total_liters(containers: tuple, liters: int) -> bool:
    result: int = 0
    for num in containers:
        result += num
    return result == liters


def get_combinations(containers: tuple) -> list[tuple]:
    for i in range(len(containers)):
        combs = combinations(containers, i + 1)

        for comb in combs:
            yield comb


def get_valid_combinations(containers: tuple, liters: int) -> list:
    combs = get_combinations(containers)
    result: list = list()
    for comb in combs:
        if is_total_liters(comb, liters):
            result.append(comb)

    return result


if __name__ == "__main__":
    path = "puzzle_day17.txt"
    liters = 150

    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    if lines[-1].strip() == "":
        lines = lines[:-1]

    containers_l: list = list()
    for line in lines:
        containers_l.append(int(line))

    containers: tuple = tuple(containers_l)

    # print(containers)
    # print(list(get_combinations(containers)))
    # print(list(get_valid_combinations(containers, liters)))

    valid_combinations = get_valid_combinations(containers, liters)
    print(f"There are {len(valid_combinations)} ways to fit exactly {liters} liters")

    min_length: int = 0
    for comb in valid_combinations:
        if min_length == 0:
            min_length = len(comb)

        if len(comb) < min_length:
            min_length = len(comb)

    min_containers = list(filter(lambda x: len(x) == min_length, valid_combinations))
    print(
        f"There are {len(min_containers)} ways to fit exactly {liters} liters, with the least number of containers"
    )
