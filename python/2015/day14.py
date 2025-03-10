from pathlib import Path


def parse_reindeer(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    result: dict = dict()
    for line in lines:
        parsed = line.split(" ")
        result[parsed[0]] = {
            "speed": int(parsed[3]),
            "run_time": int(parsed[6]),
            "rest_time": int(parsed[13]),
        }

    # # print(result)
    return result


def race_reindeer(data: dict, seconds: int, cumulative: bool = False):
    """
    create a schedule for each reindeer over time
    the schedule will be seconds long
    """

    for key in data.keys():
        schedule = list()
        run_time = data[key]["run_time"]
        rest_time = data[key]["rest_time"]
        speed = data[key]["speed"]

        for i in range(seconds):
            if run_time > 0:
                schedule.append(speed)
                # print(f"appended {speed}")
                run_time -= 1

            elif run_time == 0 and rest_time > 0:
                schedule.append(0)
                # print(f"appended 0")
                rest_time -= 1

            if run_time == 0 and rest_time == 0:
                run_time = data[key]["run_time"]
                rest_time = data[key]["rest_time"]

            # print(f"{run_time=} {rest_time=} {i+1=}, {len(schedule)}")

            if len(schedule) != i + 1:
                raise Exception(
                    f"schedule is not same size as seconds: length of schedule: {len(schedule)}, current second: {i + 1}"
                )

        if cumulative:
            cum_schedule: list = list()

            total: int = 0
            for second in schedule:
                total += second
                cum_schedule.append(total)

            schedule = cum_schedule

        data[key]["schedule"] = schedule

    return data


def calculate_race_points(data: dict, seconds: int) -> dict:
    race = race_reindeer(data, seconds, True)

    for i in range(seconds):
        leader: int = 0
        for reindeer, data in race.items():
            if data["schedule"][i] > leader:
                leader = data["schedule"][i]

        for reindeer, data in race.items():
            if "points" not in race[reindeer].keys():
                race[reindeer]["points"] = list()

            if data["schedule"][i] == leader:
                race[reindeer]["points"].append(1)

    return race


if __name__ == "__main__":
    path = Path("puzzle_day14.txt")
    data = parse_reindeer(path)
    race = race_reindeer(data, 2503)

    winner = max(race, key=lambda x: sum(race[x]["schedule"]))

    print("Total Distance")
    for reindeer, values in race.items():
        print(f'{reindeer.ljust(10)} total travel = {sum(values["schedule"])}', end="")
        if reindeer == winner:
            print("    <----- WINNER")
        else:
            print()

    race = calculate_race_points(data, 2503)

    winner = max(race, key=lambda x: sum(race[x]["points"]))

    print()
    print("Points")
    for reindeer, values in race.items():
        print(f'{reindeer.ljust(10)} total travel = {sum(values["points"])}', end="")
        if reindeer == winner:
            print("    <----- WINNER")
        else:
            print()
