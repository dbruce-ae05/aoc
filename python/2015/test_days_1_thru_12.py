from day2 import (
    bow_length_for_box,
    wrapping_paper_for_box,
)
from day3 import follow_instr, follow_instr2, str_chunks
from day4 import get_lowest_number_with_hash_leading_zeroes
from day5 import is_nice, is_nice2
from day6 import init_grid, perform_instr
from day7 import is_numeric_result, wire_it_up
from day8 import len_str_literal, len_str_memory
from day9 import get_routes
from day10 import look_and_say
from day11 import (
    check_letters,
    check_pairs,
    check_straight,
    chrnum,
    dec2base,
    increment_string,
    ordstr,
    reversed,
    valid_password,
)
from day12 import walk


def test_wrapping_paper_for_box():
    assert 58 == wrapping_paper_for_box(2, 3, 4)
    assert 43 == wrapping_paper_for_box(1, 1, 10)


def test_bow_length_for_box():
    assert 34 == bow_length_for_box(2, 3, 4)
    assert 14 == bow_length_for_box(1, 1, 10)


def test_follow_instr():
    assert 2 == follow_instr(">")
    assert 4 == follow_instr("^>v<")
    assert 2 == follow_instr("^v^v^v^v^v")


def test_str_chunks():
    input = "abcdef"
    frm = 0
    to = 2

    for val in str_chunks(input, 2):
        assert val == input[frm:to]
        frm += 2
        to += 2


def test_follow_instr2():
    assert 3 == follow_instr2("^v")
    assert 3 == follow_instr2("^>v<")
    assert 11 == follow_instr2("^v^v^v^v^v")


def test_check_hash():
    assert 609043 == get_lowest_number_with_hash_leading_zeroes("abcdef", 5)
    assert 1048970 == get_lowest_number_with_hash_leading_zeroes("pqrstuv", 5)


def test_is_nice():
    assert is_nice("ugknbfddgicrmopn")
    assert is_nice("aaa")
    assert not is_nice("jchzalrnumimnmhp")
    assert not is_nice("haegwjzuvuyypxyu")
    assert not is_nice("dvszwmarrgswjxmb")


def test_is_nice2():
    assert is_nice2("qjhvhtzxzqqjkmpb")
    assert is_nice2("xxyxx")
    assert not is_nice2("uurcxstgmygtbstg")
    assert not is_nice2("ieodomkazucvgmuy")
    assert not is_nice2("aaa")
    assert is_nice2("yyxyy")
    assert is_nice2("jfadfjasdfjxfjjfkak")
    assert not is_nice2("aabbaabbaa")
    assert is_nice2("aaaa")


def test_perform_instr():
    grid = init_grid(1000, 1000)
    grid = perform_instr("turn on 0,0 through 999,999", grid)
    assert sum(grid.values()) == 1000 * 1000


def test_is_numeric_result():
    wires = dict()
    wires["x"] = 123
    wires["y"] = 124
    assert is_numeric_result("123 -> x", wires)
    assert is_numeric_result("124 -> y", wires)
    assert is_numeric_result("x AND y -> z", wires)
    assert is_numeric_result("x OR y -> z", wires)
    assert not is_numeric_result("a OR x -> z", wires)
    assert not is_numeric_result("a -> x", wires)
    assert is_numeric_result("x RSHIFT 2 -> f", wires)
    assert not is_numeric_result("q RSHIFT 3 -> w", wires)
    assert is_numeric_result("x LSHIFT 3 -> g", wires)
    assert not is_numeric_result("r LSHIFT 3 -> g", wires)
    assert is_numeric_result("NOT x -> g", wires)
    assert not is_numeric_result("NOT q -> g", wires)


def test_wire_it_up():
    assert wire_it_up("123 -> x", dict()) == ("x", 123)
    assert wire_it_up("NOT 123 -> y", dict()) == ("y", 65412)
    assert wire_it_up("123 LSHIFT 2 -> f", dict()) == ("f", 492)

    wires = dict()
    wires["x"] = 123
    wires["y"] = 124
    assert wire_it_up("123 -> x", wires) == ("x", 123)
    assert wire_it_up("x AND y -> d", wires) == ("d", 120)
    assert wire_it_up("x LSHIFT y -> a", wires) == (
        "a",
        2615920695704714437874692294631718125568,
    )
    assert wire_it_up("x RSHIFT y -> a", wires) == ("a", 0)

    wires = dict()

    key, value = wire_it_up("123 -> x", wires)
    wires[key] = value
    key, value = wire_it_up("456 -> y", wires)
    wires[key] = value
    key, value = wire_it_up("x AND y -> d", wires)
    wires[key] = value
    key, value = wire_it_up("x OR y -> e", wires)
    wires[key] = value
    key, value = wire_it_up("x LSHIFT 2 -> f", wires)
    wires[key] = value
    key, value = wire_it_up("y RSHIFT 2 -> g", wires)
    wires[key] = value
    key, value = wire_it_up("NOT x -> h", wires)
    wires[key] = value
    # print(key, value)
    key, value = wire_it_up("NOT y -> i", wires)
    wires[key] = value

    assert wires["d"] == 72
    assert wires["e"] == 507
    assert wires["f"] == 492
    assert wires["g"] == 114
    assert wires["h"] == 65412
    assert wires["i"] == 65079


def test_string_literal():
    str1 = r'""'
    str2 = r'"abc"'
    str3 = r'"aaa\"aaa"'
    str4 = r'"\x27"'

    assert len_str_literal(str1) == 2
    assert len_str_literal(str2) == 5
    assert len_str_literal(str3) == 10
    assert len_str_literal(str4) == 6


def test_string_memory():
    str1 = r'""'
    str2 = r'"abc"'
    str3 = r'"aaa\"aaa"'
    str4 = r'"\x27"'

    assert len_str_memory(str1) == 0
    assert len_str_memory(str2) == 3
    assert len_str_memory(str3) == 7
    assert len_str_memory(str4) == 1


# def test_string_encode():
#
#     str1 = r'""'
#     str2 = r'"abc"'
#     str3 = r'"aaa\"aaa"'
#     str4 = r'"\x27"'
#
#     assert len_str_encode(str1) == 6
#     assert len_str_encode(str2) == 9
#     assert len_str_encode(str3) == 10
#     assert len_str_encode(str4) == 11


def test_route_length():
    distances = [
        "London to Dublin = 464",
        "London to Belfast = 518",
        "Dublin to Belfast = 141",
    ]

    keys = [
        "Dublin -> London -> Belfast",
        "London -> Dublin -> Belfast",
        "London -> Belfast -> Dublin",
        "Dublin -> Belfast -> London",
        "Belfast -> Dublin -> London",
        "Belfast -> London -> Dublin",
    ]

    values = [982, 605, 659, 659, 605, 982]

    routes = get_routes(distances)

    for key in routes.keys():
        # print(key)
        assert key in keys

    for value in routes.values():
        # print(value)
        assert value in values


def test_look_and_say():
    assert look_and_say("1") == "11"
    assert look_and_say("11") == "21"
    assert look_and_say("21") == "1211"
    assert look_and_say("1211") == "111221"
    assert look_and_say("111221") == "312211"


def test_reversed():
    assert reversed("abc") == "cba"
    assert reversed("cba") == "abc"
    assert reversed("ab") == "ba"
    assert reversed("ba") == "ab"


def test_ordstr():
    assert ordstr("a") == [ord("a")]
    assert ordstr("ab") == [ord("a"), ord("b")]
    assert ordstr("abc") == [ord("a"), ord("b"), ord("c")]


def test_chrnum():
    assert chrnum([97]) == "a"
    assert chrnum([97, 98]) == "ab"
    assert chrnum([97, 98, 99]) == "abc"


def test_increment_string():
    assert increment_string("a") == "b"
    assert increment_string("b") == "c"
    assert increment_string("z") == "aa"
    assert increment_string("aa") == "ab"
    assert increment_string("xx") == "xy"
    assert increment_string("xy") == "xz"
    assert increment_string("xz") == "ya"
    assert increment_string("ya") == "yb"
    assert increment_string("zz") == "aaa"
    assert increment_string("abcdefzz") == "abcdegaa"


def test_check_straight():
    assert check_straight("abc")
    assert not check_straight("abd")
    assert check_straight("xyz")
    assert not check_straight("yza")
    assert check_straight("cde")


def test_check_letters():
    assert check_letters("abc")
    assert not check_letters("abci")
    assert not check_letters("abcl")
    assert not check_letters("abco")
    assert not check_letters("abcil")
    assert not check_letters("abcio")
    assert not check_letters("abciol")


def test_check_pair():
    assert not check_pairs("abac")
    assert not check_pairs("acac")
    assert check_pairs("aabb")
    assert check_pairs("bbczz")
    assert check_pairs("ccdyy")
    assert check_pairs("ggbaa")
    assert check_pairs("zzaa")
    assert not check_pairs("aaa")


def test_valid_password():
    assert not valid_password("hijklmmn")
    assert not valid_password("abbceffg")
    assert not valid_password("abbcegjk")
    assert valid_password("aabbabc")


def test_dec2base():
    assert dec2base(10, 10) == [1, 0]
    assert dec2base(8, 16) == [8]
    assert dec2base(25, 25) == [1, 0]
    assert dec2base(10, 25) == [10]


def test_next_password():
    pass
    # commenting out b/c these tests take a long time
    # assert next_password("abcdefgh") == "abcdffaa"
    # assert next_password("ghijklmn") == "ghjaabcc"


def test_walk():
    iterable = {"a": [1, 2, 3], "b": {"c": [1, 2, 3]}}
    assert walk(iterable) == [1, 2, 3, 1, 2, 3]

    iterable = [1, 2, 3]
    assert walk(iterable) == [1, 2, 3]

    iterable = {"a": 2, "b": 4}
    assert walk(iterable) == [2, 4]

    iterable = [[[3]]]
    assert walk(iterable) == [3]

    iterable = {"a": {"b": 4}, "c": -1}
    assert walk(iterable) == [4, -1]

    iterable = []
    assert walk(iterable) == []

    iterable = {}
    assert walk(iterable) == []

    iterable = [1, 2, 3]
    assert walk(iterable, excludestr="red") == [1, 2, 3]

    iterable = [1, {"c": "red", "b": 2}, 3]
    assert walk(iterable, excludestr="red") == [1, 3]

    iterable = {"d": "red", "e": [1, 2, 3, 4], "f": 5}
    assert walk(iterable, excludestr="red") == []
