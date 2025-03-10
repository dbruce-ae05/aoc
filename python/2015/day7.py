from pathlib import Path

"""
Need a different strategy here.  Perhaps loop through the lines looking for
an instruction that yields a number, then remove that line from the list
then do it again.

"""


def eight_bit(number: int) -> int:
    if number < 0:
        number += 2**16
    return number


def wire_it_up(instruction: str, wires: dict) -> tuple:
    parts = instruction.split("->")
    key = parts[1].strip()
    instr = parts[0].strip().split(" ")

    if len(instr) == 1:
        if instr[0] in wires.keys():
            instr[0] = wires[instr[0]]

        return (key, eight_bit(int(instr[0])))

    if len(instr) == 2:
        if instr[1] in wires.keys():
            instr[1] = wires[instr[1]]

        if instr[0] == "NOT":
            return (key, eight_bit(~int(instr[1])))

    if instr[0] in wires.keys():
        instr[0] = wires[instr[0]]

    if instr[2] in wires.keys():
        instr[2] = wires[instr[2]]

    match instr[1]:
        case "LSHIFT":
            return (key, eight_bit(int(instr[0]) << int(instr[2])))
        case "RSHIFT":
            return (key, eight_bit(int(instr[0]) >> int(instr[2])))
        case "AND":
            return (key, eight_bit(int(instr[0]) & int(instr[2])))
        case "OR":
            return (key, eight_bit(int(instr[0]) | int(instr[2])))


def is_numeric_result(instruction: str, wires: dict) -> bool:
    parts = instruction.split("->")
    # key = parts[1].strip()
    instr = parts[0].strip().split(" ")

    if len(instr) == 1:
        if instr[0].isnumeric() or instr[0] in wires.keys():
            return True

        return False

    if len(instr) == 2:
        if instr[0] == "NOT":
            if instr[1].isnumeric():
                return True

            if instr[1] in wires.keys():
                return True

        return False

    if not isinstance(instr[0], int):
        if instr[0].isnumeric():
            instr[0] = int(instr[0])

    if not isinstance(instr[2], int):
        if instr[2].isnumeric():
            instr[2] = int(instr[2])

    if instr[0] in wires.keys() and isinstance(instr[2], int):
        return True

    if isinstance(instr[0], int) and instr[2] in wires.keys():
        return True

    if instr[0] in wires.keys() and instr[2] in wires.keys():
        return True

    return False


if __name__ == "__main__":
    path = Path("puzzle_day7.txt")

    with open(path, "r") as f:
        lines = f.read().split("\n")

    lines = lines[:-1]
    wires = dict()

    while len(lines) != 0:
        for i, line in enumerate(lines):
            if is_numeric_result(line, wires):
                # print(f'Line ({line}) results in number')

                key, value = wire_it_up(lines.pop(i), wires)
                wires[key] = value

    # for key, value in wires.items():
    #     print(f'{key} = {value}')

    print(f'Wire a = {wires["a"]}')

    with open(path, "r") as f:
        lines = f.read().split("\n")

    lines = lines[:-1]

    for i, line in enumerate(lines):
        parts = line.split("->")
        key = parts[1].strip()
        instr = parts[0].strip().split(" ")

        if key == "b":
            lines[i] = f"{wires['a']} -> b"

    wires = dict()

    while len(lines) != 0:
        for i, line in enumerate(lines):
            if is_numeric_result(line, wires):
                # print(f'Line ({line}) results in number')

                key, value = wire_it_up(lines.pop(i), wires)
                wires[key] = value

    # for key, value in wires.items():
    #     print(f'{key} = {value}')

    print(f'Wire a = {wires["a"]}, if wire b is overridden with {wires["a"]}')
    print(f'Wire b = {wires["b"]}')
