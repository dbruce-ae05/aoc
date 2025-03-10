from itertools import permutations
from pathlib import Path


def wrapping_paper_for_box(length: int, width: int, height: int) -> int:
    length = int(length)
    width = int(width)
    height = int(height)

    perms = permutations([length, width, height], 2)

    perm_results = list()
    for i, j in perms:
        perm_results.append(i * j)

    min_area = min(perm_results)

    return 2 * length * width + 2 * width * height + 2 * height * length + min_area


def bow_length_for_box(length: int, width: int, height: int) -> int:
    length = int(length)
    width = int(width)
    height = int(height)

    perms = permutations([length, width, height], 2)

    perm_results = list()
    for i, j in perms:
        perm_results.append(2 * i + 2 * j)

    min_length = min(perm_results)

    return length * width * height + min_length


if __name__ == "__main__":
    path = Path("puzzle_day2.txt")

    with open(path, "r") as f:
        boxes = f.readlines()

    areas = list()
    ribbon = list()
    for box in boxes:
        areas.append(wrapping_paper_for_box(*box.split("x")))
        ribbon.append(bow_length_for_box(*box.split("x")))

    print(f"Total square feet of wrapping paper to order: {sum(areas)}")
    print(f"Total length of ribbon to order: {sum(ribbon)}")
