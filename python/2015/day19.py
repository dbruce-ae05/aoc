def calibrate(molecule: str, replacements: list[tuple]) -> set:
    results: set = set()

    for orig, new in replacements:
        start: int = 0
        end: int = start + len(orig)

        while end <= len(molecule) + 1:
            if molecule[start:end] == orig:
                results.add(molecule[0:start] + new + molecule[end:])

            start += 1
            end = start + len(orig)

    return results


def make_molecule(start: str, finish: str, replacements: list[tuple]) -> set:
    molecules: set = set()
    molecules.add(start)
    cnt: int = 1
    while True:
        new_molecules: set = set()
        for molecule in molecules:
            new_molecules.update(calibrate(molecule, replacements))

        molecules = new_molecules

        if finish in molecules:
            break

        cnt += 1
        if cnt % 1 == 0:
            # print(f"Iteration: {cnt}, potential molecules: {len(molecules)}")
            pass

    return cnt


if __name__ == "__main__":
    path = "puzzle_day19.txt"

    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    replacements: list[tuple] = list()
    flag: bool = False
    for line in lines:
        if line and not flag:
            replacement = line.split("=>")
            replacement = [r.strip() for r in replacement]
            replacements.append((replacement[0], replacement[1]))
        else:
            flag = True
            continue

    if flag:
        molecule = line

    result = calibrate(molecule, replacements)

    print(f"There are {len(result)} distinct molecules")

    result = make_molecule("e", molecule, replacements)
    print(f"The fewest number of steps to make the medice is {result}")
