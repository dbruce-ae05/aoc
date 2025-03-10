from day2 import possible_reports, read_reports, report_safe


def test_read_reports():
    reports = read_reports("day2_test_data.txt")

    assert reports[0] == [7, 6, 4, 2, 1]
    assert reports[1] == [1, 2, 7, 8, 9]
    assert reports[2] == [9, 7, 6, 2, 1]
    assert reports[3] == [1, 3, 2, 4, 5]
    assert reports[4] == [8, 6, 4, 4, 1]
    assert reports[5] == [1, 3, 6, 7, 9]


def test_report_safe():
    assert report_safe([7, 6, 4, 2, 1])
    assert not report_safe([1, 2, 7, 8, 9])
    assert not report_safe([9, 7, 6, 2, 1])
    assert not report_safe([1, 3, 2, 4, 5])
    assert not report_safe([8, 6, 4, 4, 1])
    assert report_safe([1, 3, 6, 7, 9])


def test_possible_reports():
    assert possible_reports([7, 6, 5]) == [[7, 6, 5], [6, 5], [7, 5], [7, 6]]
