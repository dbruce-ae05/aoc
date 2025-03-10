from pathlib import Path


def read_reports(path: Path) -> list:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result: list = list()
    for line in lines:
        levels = line.strip().split(" ")
        for i, _ in enumerate(levels):
            levels[i] = int(levels[i])

        result.append(levels)

    return result


def report_safe(report: list) -> bool:
    temp = None
    increasing: bool = False
    decreasing: bool = False
    difference: bool = False

    for level in report:
        if temp is None:
            temp = level
            continue

        if temp > level:
            increasing = True
        else:
            increasing = False
            break

        temp = level

    temp = None
    for level in report:
        if temp is None:
            temp = level
            continue

        if temp < level:
            decreasing = True
        else:
            decreasing = False
            break

        temp = level

    temp = None
    for level in report:
        if temp is None:
            temp = level
            continue

        diff = abs(temp - level)
        if diff >= 1 and diff <= 3:
            difference = True
        else:
            difference = False
            break

        temp = level

    return (increasing or decreasing) and difference


def possible_reports(report: list) -> list[list]:
    result: list = list()

    result.append(report)

    for i, _ in enumerate(report):
        temp = report.copy()
        temp.pop(i)
        result.append(temp)

    return result


if __name__ == "__main__":
    reports = read_reports("day2_puzzle.txt")

    safe_reports: int = 0
    safe_reports_pd: int = 0
    for report in reports:
        if report_safe(report):
            safe_reports += 1
        else:
            for possible_report in possible_reports(report):
                if report_safe(possible_report):
                    safe_reports_pd += 1
                    break

    print(f"There are {safe_reports} safe reports")
    print(
        f"There are {safe_reports_pd + safe_reports} safe reports with Problem Dampener"
    )
