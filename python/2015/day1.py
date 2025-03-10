from pathlib import Path

if __name__ == "__main__":
    path = Path("puzzle_day1.txt")

    with open(path, "r") as f:
        instructions = f.readline()

    # print(type(instructions))
    print(f"The instructions are {len(instructions)} characters long")

    cnt = 0
    char_cnt = 1
    basement_position = list()
    for char in instructions:
        if char == "(":
            cnt += 1
        if char == ")":
            cnt -= 1

        if cnt < 0:
            basement_position.append(char_cnt)

        char_cnt += 1

    print(f"Santa should go to floor: {cnt}")
    print(
        f"The position of the character that causes Santa to first enter the basement is {basement_position[0]}"
    )
