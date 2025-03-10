from collections import Counter

"""
approach:
    the attributes will be the key

"""
if __name__ == "__main__":
    path = "puzzle_day16.txt"

    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    lines = lines[:-1]

    search_dicts: dict = dict()

    for line in lines:
        sue = int(line[: line.find(":")].replace("Sue ", ""))
        attrs = line[line.find(":") + 1 :].strip().split(",")
        attrs = [attr.strip() for attr in attrs]

        for attr in attrs:
            attr = attr.split(":")
            attr = [x.strip() for x in attr]

            if attr[0] not in search_dicts.keys():
                search_dicts[attr[0]] = dict()

            if attr[1] not in search_dicts[attr[0]].keys():
                search_dicts[attr[0]][attr[1]] = set()

            search_dicts[attr[0]][attr[1]].add(sue)

    target_dicts: dict = {
        "children": "3",
        "cats": "7",
        "samoyeds": "2",
        "pomeranians": "3",
        "akitas": "0",
        "vizslas": "0",
        "goldfish": "5",
        "trees": "3",
        "cars": "2",
        "perfumes": "1",
    }

    sues: list = list()
    for key, value in target_dicts.items():
        # print(search_dicts[key][value])
        sues.append(search_dicts[key][value])

    cum_sue: list = list()

    for sue in sues:
        cum_sue.extend(list(sue))

    c = Counter(cum_sue)
    print(max(c.items(), key=lambda x: x[1]))
