from collections import Counter
from pathlib import Path

from day6 import init_grid, show_grid


def read_grid(path: Path = None, input_str: str = None) -> dict:
    if path:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.read().strip().split("\n")

    if input_str:
        lines = input_str.strip().split("\n")

    grid: dict = dict()
    row: int = 0
    col: int = 0
    for line in lines:
        col = 0
        for char in line:
            grid[(row, col)] = char
            col += 1
        row += 1

    return grid


def get_neighbors(index: tuple, grid: dict, max_row: int == None, max_col: int = None):
    if max_row is None:
        max_row = max([row for row, col in grid.keys()])
    if max_col is None:
        max_col = max([col for row, col in grid.keys()])

    row = index[0]
    col = index[1]

    min_i = max(0, row - 1)
    min_j = max(0, col - 1)
    max_i = min(max_row + 1, row + 2)
    max_j = min(max_col + 1, col + 2)

    neighbors: list = list()
    for i in range(min_i, max_i):
        for j in range(min_j, max_j):
            if (i, j) != index:
                neighbors.append(grid[(i, j)])

    return neighbors


def next_grid(
    grid: dict, max_row: int = None, max_col: int = None, corners: bool = False
) -> dict:
    if max_row is None:
        max_row = max([row for row, col in grid.keys()])
    if max_col is None:
        max_col = max([col for row, col in grid.keys()])

    on = "#"
    off = "."
    result: dict = dict()

    for i in range(max_row + 1):
        for j in range(max_col + 1):
            neighbors = get_neighbors((i, j), grid, max_row, max_col)
            c = Counter(neighbors)

            if grid[(i, j)] == on:
                if c[on] == 2 or c[on] == 3:
                    result[(i, j)] = on
                else:
                    result[(i, j)] = off

            if grid[(i, j)] == off:
                if c[on] == 3:
                    result[(i, j)] = on
                else:
                    result[(i, j)] = off

            if c[off] > 5:
                result[(i, j)] == on

    if corners:
        result[(0, 0)] = on
        result[(0, max_col)] = on
        result[(max_row, 0)] = on
        result[(max_row, max_col)] = on

    return result


def clear():
    # os.system("clear")
    print("\033[1000A")


if __name__ == "__main__":
    path = "day18_tst_data_5.txt"
    on = "#"
    off = "."

    grid = read_grid(path=path)

    max_row = max([row for row, col in grid.keys()])
    max_col = max([col for row, col in grid.keys()])

    clear()
    show_grid(grid)

    for i in range(100):
        grid = next_grid(grid, max_row, max_col, corners=True)
        print(f"generated grid {i}")
        clear()
        show_grid(grid)
        # time.sleep(0.5)

    c = Counter(grid.values())

    print(f"There are {c[on]} lights ON, and {c[off]} lights OFF")
