def single_digit(number: int) -> int:
    while number > 9:
        new_number = 0
        while number > 9:
            two_digits = number % 100
            new_number = new_number * 10 + abs(two_digits // 10 - two_digits % 10)
            number //= 10
        number = new_number
    return number


if __name__ == "__main__":
    print(single_digit(584))
    print(single_digit(5))
    print(single_digit(98765))
    print(single_digit(128745))
