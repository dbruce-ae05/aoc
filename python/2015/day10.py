def look_and_say(num: str) -> int:
    num = str(num)

    result: str = str()
    current: str = str()
    cnt: int = 0

    for s in num:
        if current == str():
            current = s

        if current == s:
            cnt += 1
        else:
            result += str(cnt) + current
            current = s
            cnt = 1

    result += str(cnt) + current

    return result


if __name__ == "__main__":
    original_input = 1113122113

    iterations = [40, 50]

    for iters in iterations:
        input = original_input

        for i in range(iters):
            input = look_and_say(input)

        print(
            f"With puzzle {original_input=}, after {iters} iterations the length of  look and say is {len(input)}"
        )
