from day_two_input import puzzle_input


def get_invalid_password_count() -> int:

    return sum([1 for line in puzzle_input if _is_valid(*line.split(":"))])


def _is_valid(policy, password) -> bool:

    password = password.strip()
    first_second_policy, letter = policy.split(" ")
    first, second = first_second_policy.split("-")

    return (password[int(first) - 1] == letter) ^ (password[int(second) - 1] == letter)


if __name__ == "__main__":

    print(get_invalid_password_count())
