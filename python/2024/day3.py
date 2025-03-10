import re
from pathlib import Path


def parse_corrupt_data(path: Path, test_for_enable: bool = False) -> list:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result: list = list()
    for line in lines:
        line = line.strip()

        muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)

        if test_for_enable:
            muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", line)

        result.extend(muls)

    if test_for_enable:
        old_result = result.copy()
        result = list()
        flag: bool = True
        for arg in old_result:
            test = arg.split("(")[0]
            match test:
                case "do":
                    flag = True
                case "don't":
                    flag = False
                case "mul":
                    if flag:
                        result.append(arg)

    return result


def calculate_mul(args: list) -> int:
    total: int = 0
    for arg in args:
        if "mul(" == arg[:4]:
            arg = arg[4:-1].split(",")
            total += int(arg[0]) * int(arg[1])

    return total


if __name__ == "__main__":
    path = "day3_puzzle.txt"
    muls = parse_corrupt_data(path)
    total = calculate_mul(muls)

    print(f"The total is: {total}")

    muls = parse_corrupt_data(path, True)
    total = calculate_mul(muls)
    print(f"The total, with enablement, is: {total}")
