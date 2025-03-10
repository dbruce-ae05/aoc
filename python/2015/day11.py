import string


def dec2base(num: int, base: int) -> list:
    result = list()
    if num == 0:
        result.append(0)
        return result

    while num:
        result.append(int(num % base))
        num //= base

    # reverse the list
    result = result[::-1]
    return result


def dec2base_str(
    num: int, base: int, representations: list = string.digits + string.ascii_uppercase
) -> str:
    if base > len(representations):
        raise ValueError(
            f"Representations must have same length >= base, {base=}, length of representations={len(representations)}"
        )

    conv_num = dec2base(num, base)
    result: str = str()

    for num in conv_num:
        result += representations[num]

    return result


def reversed(arg: str) -> str:
    return arg[::-1]


def ordstr(arg: str) -> list:
    result: list = list()
    for s in arg:
        result.append(ord(s))
    return result


def chrnum(arg: list) -> str:
    result = str()
    for num in arg:
        result += chr(num)
    return result


def increment_string(password: str) -> str:
    plist: list = list()
    plist = ordstr(reversed(password))

    plist[0] += 1

    blnroll = False
    for i, num in enumerate(plist):
        if blnroll:
            plist[i] += 1
            blnroll = False

        if plist[i] > ord("z"):
            plist[i] = ord("a")
            blnroll = True

    if blnroll:
        plist.append(ord("a"))

    return reversed(chrnum(plist))


def check_straight(password: str) -> bool:
    ords = ordstr(password)

    for i, num in enumerate(ords):
        if i + 3 > len(ords):
            break

        if ords[i + 2] == ords[i + 1] + 1 and ords[i + 1] == ords[i] + 1:
            return True

    return False


def check_letters(password: str) -> bool:
    if "i" in password or "o" in password or "l" in password:
        return False
    return True


def check_pairs(password: str) -> bool:
    test_pair: str
    tests: dict = dict()
    for i in range(97, 123):
        test_pair = chr(i) + chr(i)

        if test_pair in password:
            tests[test_pair] = password.count(test_pair)

    if sum(tests.values()) >= 2:
        return True

    return False


def valid_password(password: str) -> bool:
    if check_straight(password) and check_pairs(password) and check_letters(password):
        return True

    return False


def next_password(password: str) -> str:
    password = increment_string(password)
    while not valid_password(password):
        password = increment_string(password)

    return password


if __name__ == "__main__":
    passwords: list = list()
    passwords.append("hxbxwxba")
    for i in range(10):
        passwords.append(next_password(passwords[-1]))

    for i, password in enumerate(passwords):
        print(f"Password {i} is {password}")
