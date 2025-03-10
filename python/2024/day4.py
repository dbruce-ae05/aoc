import re
from pathlib import Path


def read_puzzle(path: Path) -> list:
    with open(path, "r", encoding="utf8") as f:
        lines = f.readlines()

    result: list = list()
    for line in lines:
        result.append(line.strip())

    return result


def test_grid(grid: list) -> bool:
    rows = len(grid)

    for row in grid:
        if len(row) != rows:
            return False

    return True


def get_horizontals(grid: list) -> list:
    for line in grid:
        yield line


def get_verticals(grid: list) -> list:
    result: str = str()

    for cnt in range(0, len(grid[0])):
        for line in grid:
            result += line[cnt]

        yield result
        result = str()


def get_diagonals(grid: list) -> list:
    result: list = list()
    rows = len(grid)

    def test_coordinates(x: int, y: int, max: int) -> bool:
        if x >= 0 and y >= 0 and x < max and y < max:
            return True
        return False

    # get positive/negative slope diagonals (y = mx + b, m = 1 => y = x + b)
    # y = x + b, where b is the range from 0 to row/column count

    for b in range(2 * rows):
        diag: list = list()
        for x in range(2 * rows):
            y = -x + b

            if test_coordinates(x, y, rows):
                diag.append(grid[x][y])

        if diag:
            result.append(diag)

    for b in range(2 * rows, -2 * rows, -1):
        diag: list = list()
        for x in range(2 * rows):
            y = x + b

            if test_coordinates(x, y, rows):
                diag.append(grid[y][x])

        if diag:
            result.append(diag)

    return result


def count_xmas(path: Path) -> int:
    grid = read_puzzle(path)
    potentials: list = list()
    potentials.extend(list(get_horizontals(grid)))
    potentials.extend(list(get_verticals(grid)))
    potentials.extend(list(get_diagonals(grid)))

    cnt: int = 0

    for potential in potentials:
        test_string = "".join(potential)
        for_hits = re.findall(r"XMAS", test_string)
        bac_hits = re.findall(r"SAMX", test_string)

        cnt += len(for_hits) + len(bac_hits)

    return cnt


if __name__ == "__main__":
    hits = count_xmas("day4_puzzle.txt")

    print(f'There are {hits} occurrences of "XMAS"')
