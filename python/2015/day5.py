import string
from pathlib import Path
from day3 import str_chunks


def is_nice(input: str) -> bool:
    if "ab" in input or "cd" in input or "pq" in input or "xy" in input:
        return False

    vowel_count = 0
    for vowel in "aeiou":
        temp = input.replace(vowel, "")
        vowel_count += len(input) - len(temp)

    if vowel_count < 3:
        return False

    double_letter_flag = False
    for letter in string.ascii_lowercase:
        test = letter + letter

        if test in input:
            double_letter_flag = True

    if not double_letter_flag:
        return False

    return True


def is_nice2(input: str) -> bool:
    fm = 0
    to = 2
    pairflag = False
    while to <= len(input):
        start = input[:fm]
        end = input[to:]
        pair = input[fm:to]

        # print(f'{start=} {pair=} {end=}')

        fm += 1
        to += 1

        if pair in start + end:
            pairflag = True
            break

    if not pairflag:
        return False

    repeatflag = False
    for i, char in enumerate(input):
        if i + 2 >= len(input):
            break

        if input[i] == input[i + 2]:
            repeatflag = True
            break

    return repeatflag


if __name__ == "__main__":
    path = Path("puzzle_day5.txt")

    with open(path, "r") as f:
        lines = f.read().split("\n")
    lines = lines[:-1]

    result: list = list()
    result2: list = list()
    for line in lines:
        if is_nice(line):
            result.append(line)

        if is_nice2(line):
            result2.append(line)

    print(f"There are {len(result)} nice strings")
    print(f"There are {len(result2)} nice strings2")
