from day1 import calculate_distance, calculate_similarity, read_data


def test_read_data():
    truth = [(1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 9)]
    test = list(read_data("day1_test_data.txt"))

    assert truth == test


def test_calculate_distance():
    test = list(read_data("day1_test_data.txt"))

    assert 11 == calculate_distance(test)


def test_calculate_similarity():
    a, b = list(read_data("day1_test_data.txt", 1))

    assert 31 == calculate_similarity(a, b)
