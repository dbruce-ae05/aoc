from day4 import count_xmas, get_diagonals, get_horizontals, get_verticals, read_puzzle


def test_get_horizontals():
    grid = read_puzzle("day4_test_data.txt")

    horizontals = list(get_horizontals(grid))

    assert horizontals[0] == "MMMSXXMASM"
    assert horizontals[1] == "MSAMXMSMSA"
    assert horizontals[2] == "AMXSXMAAMM"
    assert horizontals[3] == "MSAMASMSMX"
    assert horizontals[4] == "XMASAMXAMM"
    assert horizontals[5] == "XXAMMXXAMA"
    assert horizontals[6] == "SMSMSASXSS"
    assert horizontals[7] == "SAXAMASAAA"
    assert horizontals[8] == "MAMMMXMMMM"
    assert horizontals[9] == "MXMXAXMASX"


def test_get_verticals():
    grid = read_puzzle("day4_test_data.txt")

    verticals = list(get_verticals(grid))

    assert verticals[0] == "MMAMXXSSMM"
    assert verticals[1] == "MSMSMXMAAX"
    assert verticals[2] == "MAXAAASXMM"
    assert verticals[3] == "SMSMSMMAMX"
    assert verticals[4] == "XXXAAMSMMA"
    assert verticals[5] == "XMMSMXAAXX"
    assert verticals[6] == "MSAMXXSSMM"
    assert verticals[7] == "AMASAAXAMA"
    assert verticals[8] == "SSMMMMSAMS"
    assert verticals[9] == "MAMXMASAMX"


def test_get_diagonals():
    grid = [
        ["a", "b", "c", "d"],
        ["e", "f", "g", "h"],
        ["i", "j", "k", "l"],
        ["m", "n", "o", "p"],
    ]

    diagonals = list(get_diagonals(grid))

    # for diag in diagonals:
    #    print(diag)

    assert diagonals[0] == ["a"]
    assert diagonals[1] == ["b", "e"]
    assert diagonals[2] == ["c", "f", "i"]
    assert diagonals[3] == ["d", "g", "j", "m"]
    assert diagonals[4] == ["h", "k", "n"]
    assert diagonals[5] == ["l", "o"]
    assert diagonals[6] == ["p"]
    assert diagonals[7] == ["m"]
    assert diagonals[8] == ["i", "n"]
    assert diagonals[9] == ["e", "j", "o"]
    assert diagonals[10] == ["a", "f", "k", "p"]
    assert diagonals[11] == ["b", "g", "l"]
    assert diagonals[12] == ["c", "h"]
    assert diagonals[13] == ["d"]


def test_count_xmas():
    assert 18 == count_xmas("day4_test_data.txt")
