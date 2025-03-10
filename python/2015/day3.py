from pathlib import Path


def add_coordinate(pos1: tuple[int, int], pos2: tuple[int, int]) -> tuple[int, int]:
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])


def str_chunks(input: str, chunk_size: int) -> str:
    result: str = str()
    for val in input:
        result += val
        if len(result) == chunk_size:
            yield result
            result = str()


def follow_instr(instr: str) -> list[int]:
    cur_pos = (0, 0)
    directions: dict = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}

    presents: dict = dict()
    presents[cur_pos] = 1
    for char in instr:
        cur_pos = add_coordinate(cur_pos, directions[char])

        if cur_pos not in presents.keys():
            presents[cur_pos] = 0

        presents[cur_pos] += 1

    return sum([val > 0 for val in presents.values()])


def follow_instr2(instr: str) -> list[int]:
    cur_pos = (0, 0)
    cur_pos2 = (0, 0)
    directions: dict = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}

    presents: dict = dict()
    presents2: dict = dict()
    presents[cur_pos] = 1
    presents2[cur_pos2] = 1

    for santa, robosanta in str_chunks(instr, 2):
        cur_pos = add_coordinate(cur_pos, directions[santa])
        cur_pos2 = add_coordinate(cur_pos2, directions[robosanta])

        if cur_pos not in presents.keys():
            presents[cur_pos] = 0

        if cur_pos2 not in presents2.keys():
            presents2[cur_pos2] = 0

        presents[cur_pos] += 1
        presents2[cur_pos2] += 1

        # print(f'{presents=}')
        # print(f'{presents2=}')

    for key, value in presents2.items():
        if key not in presents.keys():
            presents[key] = 0

        presents[key] += value

    return sum([val > 0 for val in presents.values()])


if __name__ == "__main__":
    path = Path("puzzle_day3.txt")

    with open(path, "r") as f:
        instr = f.read()

    instr = instr.strip("\n")

    print(f"{follow_instr(instr)} homes have more than 1 present")
    print(
        f"{follow_instr2(instr)} homes have more than 1 present with Santa and RoboSanta"
    )
