from hashlib import md5


def get_lowest_number_with_hash_leading_zeroes(key: str, zeroes: int) -> int:
    flag = True

    cnt = 0
    while flag:
        temp = key + str(cnt)
        hash = md5(temp.encode()).hexdigest()

        if hash[:zeroes] == "".ljust(zeroes, "0"):
            flag = False
            break

        cnt += 1

    return cnt


if __name__ == "__main__":
    key = "ckczppom"
    print(
        f"If the key is {key}, then the answer is {get_lowest_number_with_hash_leading_zeroes(key, 5)}"
    )
    print(
        f"If the key is {key}, then the answer is {get_lowest_number_with_hash_leading_zeroes(key, 6)}"
    )
