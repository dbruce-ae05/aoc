from pathlib import Path

from day3 import calculate_mul, parse_corrupt_data


def test_parser():
    path: Path = Path("day3_test_data.txt")

    muls = parse_corrupt_data(path)

    assert muls[0] == "mul(2,4)"
    assert muls[1] == "mul(5,5)"
    assert muls[2] == "mul(11,8)"
    assert muls[3] == "mul(8,5)"


def test_calculate_mul():
    path: Path = Path("day3_test_data.txt")
    muls = parse_corrupt_data(path)
    assert calculate_mul(muls) == 161

    path = Path("day3_test_data1.txt")
    muls = parse_corrupt_data(path, True)
    assert calculate_mul(muls) == 48
