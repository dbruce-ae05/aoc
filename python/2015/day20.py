def factor(n: int) -> set:
    result: set = set()
    sqrt = int(n ** (0.5)) + 2
    for i in range(1, sqrt):
        if n % i == 0:
            result.add(i)
            result.add(int(n / i))

    result.add(n)
    result = sorted(result)
    return tuple(result)


def house_presents(house_number: int) -> int:
    factors = factor(house_number)
    # print(f"{house_number}: {factors}")
    total_presents = sum([x * 10 for x in factors])
    return total_presents


if __name__ == "__main__":
    presents = 33100000

    i = 1
    while True:
        cur_presents = house_presents(i)
        if cur_presents >= presents:
            break
        i += 1
        if i % 10000 == 0:
            print(f"{i:,}: {cur_presents:,}")

    print(f"The lowest house number to get {presents} is {i}")

    elves: dict = dict()
    i = 1
    while True:
        cum_presents: int = 0
        for f in factor(i):
            if f not in elves.keys():
                elves[f] = 0

            elves[f] += 1

            if elves[f] < 51:
                cum_presents += f * 11

        if i % 10000 == 0:
            print(f"{i:,}: {cum_presents:,}")

        if cum_presents >= presents:
            break

        i += 1

    print(
        f"The lowest house number to get at least {presents} is {i}, with the lazy elves"
    )
