from functools import reduce
from itertools import permutations
from pathlib import Path


def parse_ingredients(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    result: dict = dict()
    for line in lines:
        parsed = line.split(":")

        key = parsed[0]

        properties = parsed[1].split(",")
        properties = [item.strip() for item in properties]

        if key not in result.keys():
            result[key] = dict()

        for property in properties:
            name = property.split(" ")[0]
            value = int(property.split(" ")[1])
            result[key].update({name: value})

    return result


def score_recipe(recipe: dict, data: dict, calories: int = None) -> int:
    score: dict = dict()
    for ingredient, teaspoons in recipe.items():
        for prop, value in data[ingredient].items():
            if prop not in score.keys():
                score[prop] = 0

            score[prop] += value * teaspoons

    result: list = list()
    for prop, value in score.items():
        if prop == "calories":
            continue

        if value < 0:
            score[prop] = 0

        result.append(score[prop])

    if calories is None or calories == score["calories"]:
        return reduce(lambda a, b: a * b, result)
    else:
        return 0


def generate_possible_combinations(nums: int, total: int) -> list[tuple]:
    result: list = list()
    possibles = permutations(range(total + 1), nums)

    for possible in possibles:
        if sum(possible) == total:
            result.append(possible)

    return result


def optimize_recipe(data: dict, teaspoons: int = 100, max_calories: int = None) -> dict:
    possibles = generate_possible_combinations(len(data.keys()), teaspoons)

    scores: dict = dict()
    for possible in possibles:
        recipe: dict = dict()
        for i, key in enumerate(data.keys()):
            recipe[key] = possible[i]

        scores[possible] = score_recipe(recipe, data, max_calories)

    max_score = max(scores.values())
    optimized = [(key, value) for key, value in scores.items() if value == max_score]
    optimized = optimized[0]

    recipe: dict = dict()
    for i, key in enumerate(data.keys()):
        recipe[key] = optimized[0][i]

    result = f"{repr(recipe)} = {optimized[1]}"

    # print([f"{key}:{value}" for key, value in scores.items() if value > 0])
    return result


if __name__ == "__main__":
    path = Path("puzzle_day15.txt")

    data = parse_ingredients(path)
    result = optimize_recipe(data, 100)

    print(result)
    print()
    print("For a total calories of 500, the optimized recipe is:")
    print(optimize_recipe(data, 100, 500))
