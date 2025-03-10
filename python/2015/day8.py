from pathlib import Path


def len_str_literal(line: str) -> int:
    return len(line)


def len_str_memory(line: str) -> int:
    return len(eval(line))


def len_str_encode(line: str) -> int:
    quote_count = line.count('"')
    backs_count = line.count("\\")
    return len(line) + quote_count + backs_count

    escapes = [r"\'", r"\\", r"\n", r"\r", r"\t", r"\b", r"\f", r"\ooo", r"\xhh"]


if __name__ == "__main__":
    path = Path("puzzle_day8.txt")

    with open(path, "r") as f:
        lines = f.read().split("\n")

    lines = lines[:-1]
    strlit = list()
    strmem = list()
    strenc = list()
    for line in lines:
        strlit.append(len_str_literal(line))
        strmem.append(len_str_memory(line))
        strenc.append(len_str_encode(line))

    print(f"String Literal Lengths - String Memory Lengths = {sum(strlit)-sum(strmem)}")

    print(
        f"String Encoded Lengths - String Literal Lengths = {sum(strenc)-sum(strlit)}"
    )
