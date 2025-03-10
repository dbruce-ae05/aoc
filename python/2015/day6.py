from pathlib import Path


def perform_instr(instr: str, grid: dict) -> dict:
    instr = instr.replace("turn on", "on").replace("turn off", "off")
    instr = instr.split(" ")

    # print(f'{instr=}')

    # instr[0] = instruction (on, off, toggle)
    # instr[1] = target grid elements start range
    # instr[2] = through
    # instr[3] = target grid elements end range

    instr[1] = (int(instr[1].split(",")[0]), int(instr[1].split(",")[1]))
    instr[3] = (int(instr[3].split(",")[0]), int(instr[3].split(",")[1]))

    def set_element(action, element):
        if action == "on":
            return 1
        if action == "off":
            return 0
        if action == "toggle":
            return int(not element)

    for i in range(instr[1][0], instr[3][0] + 1):
        for j in range(instr[1][1], instr[3][1] + 1):
            grid[(i, j)] = set_element(instr[0], grid[(i, j)])

    return grid


def perform_instr2(instr: str, grid: dict) -> dict:
    instr = instr.replace("turn on", "on").replace("turn off", "off")
    instr = instr.split(" ")

    # print(f'{instr=}')

    # instr[0] = instruction (on, off, toggle)
    # instr[1] = target grid elements start range
    # instr[2] = through
    # instr[3] = target grid elements end range

    instr[1] = (int(instr[1].split(",")[0]), int(instr[1].split(",")[1]))
    instr[3] = (int(instr[3].split(",")[0]), int(instr[3].split(",")[1]))

    def set_element(action, element):
        if action == "on":
            return element + 1
        if action == "off":
            return max(element - 1, 0)
        if action == "toggle":
            return element + 2

    for i in range(instr[1][0], instr[3][0] + 1):
        for j in range(instr[1][1], instr[3][1] + 1):
            grid[(i, j)] = set_element(instr[0], grid[(i, j)])

    return grid


def init_grid(dim1: int, dim2: int, default_value=0) -> dict[tuple]:
    grid: dict = dict()
    for i in range(dim1):
        for j in range(dim2):
            grid[(i, j)] = default_value

    return grid


def show_grid(grid: dict):
    mini = min([i for i, j in grid.keys()])
    maxi = max([i for i, j in grid.keys()])
    minj = min([j for i, j in grid.keys()])
    maxj = max([j for i, j in grid.keys()])

    for i in range(mini, maxi + 1):
        for j in range(minj, maxj + 1):
            print(grid[(i, j)], end=" ")
        print()


# grid = init_grid(10, 10)
# grid = perform_instr('turn on 0,0 through 2,2', grid)
# grid = perform_instr('turn off 0,0 through 2,2', grid)
# grid = perform_instr('toggle 0,0 through 1,1', grid)
# grid = perform_instr('turn on 3,3 through 3,4', grid)
# grid = perform_instr('turn on 9,9 through 9,9', grid)
# show_grid(grid)


if __name__ == "__main__":
    path = Path("puzzle_day6.txt")

    with open(path, "r") as f:
        lines = f.read().split("\n")

    lines = lines[:-1]

    grid = init_grid(1000, 1000)
    grid1 = init_grid(1000, 1000)

    for line in lines:
        grid = perform_instr(line, grid)
        grid1 = perform_instr2(line, grid1)

        show_grid(grid)

    print(f"There are {sum(grid.values())} lights on")
    print(f"There are {sum(grid1.values())} lights on")
