import os


def read_input(path: str) -> list[int]:
    """Function to read txt as list of strings"""
    with open(path, "r") as file:
        lines: list[int] = [int(line.strip()) for line in file.readlines()]

    # Print first 5 lines
    print(f"Input values: {lines[:5]}")
    return lines


def turn_bank_into_list(bank: int) -> list[int]:
    """Turn long number (bank) into list of single digits"""
    return [int(digit) for digit in str(bank)]


# This function is not used anymore but was the one I initially used for part 01
def largest_joltage_2digits(bank: list[int]) -> int:
    """Find the largest joltage (2 digits) in a bank of batteries
    Start with 1 as first and 0 as last digit
    Kind of a sliding window, if first digit is larger or same than stored, then find the max value after that as second digit and check if now largest joltage
    If first digit already smaller than stored largest joltage, skip
    """
    max_joltage: int = 10
    n: int = len(bank)

    # Loop through all digits (except last one as we need 2 digits)
    for i in range(n - 1):
        first: int = bank[i]

        # If first digit already smaller than first digit of max_joltage, skip
        if first < max_joltage // 10:
            continue

        # Else get the max second digit of the remaining digits
        second: int = max(bank[i + 1 :])

        # Check if this is the largest joltage
        joltage: int = first * 10 + second
        if joltage > max_joltage:
            max_joltage = joltage

    return max_joltage


def largest_joltage(bank: list[int], digits: int) -> int:
    """Find the largest joltage in a bank of batteries
    Start with 1 as first and 0 as last digit
    Kind of a sliding window:
    Check if first digit is larger or same than stored
    Then take the max value of the remaining digits as next digit (make sure to have enough remaining to fill all digits). Also check if this digit is larger than stored digit at that position
    If at any point a digit is smaller than stored digit at that position, skip to next first digit
    In the end, check if now largest joltage
    """
    max_joltage_digits: list[int] = [0] * digits
    n: int = len(bank)

    # Loop through all digits
    for i in range(n - digits + 1):
        # Initialize variable to determine if all previous digits were equal to the max_joltage digits
        previous_digits_equal: bool = True
        current_joltage_digits: list[int] = []
        previous_idx: int = i - 1

        for d in range(digits):
            # Remaining digits
            remaining_digits: int = digits - d

            # Get the max from next digits but so enough digits remain
            # Also get its index so we correctly move the window afterwards
            slice: list[int] = bank[previous_idx + 1 : n - remaining_digits + 1]
            next_digit: int = max(slice)
            relative_idx: int = slice.index(next_digit)
            previous_idx += relative_idx + 1

            # If all previous digits were equal
            if previous_digits_equal:
                if next_digit < max_joltage_digits[d]:
                    break  # If this one is smaller, skip entirely
                elif next_digit > max_joltage_digits[d]:
                    previous_digits_equal = False

            current_joltage_digits.append(next_digit)

        # Check if this is the largest joltage
        if current_joltage_digits > max_joltage_digits:
            max_joltage_digits = current_joltage_digits

    return int("".join(str(d) for d in max_joltage_digits))


def sum_max_joltages(banks_list: list[list[int]], digits: int) -> None:
    """Find max joltage per bank and sum them up"""
    if digits == 2:
        max_joltages: list[int] = [
            largest_joltage_2digits(bank=bank) for bank in banks_list
        ]

        result: int = sum(max_joltages)

        print()
        print(f"Summed up maximum joltages to \033[1m{result}\033[0m")
        print("This solves the puzzle of day 3, part 1!")

    max_joltages: list[int] = [
        largest_joltage(bank=bank, digits=digits) for bank in banks_list
    ]

    result: int = sum(max_joltages)

    print()
    print(f"Summed up maximum joltages to \033[1m{result}\033[0m")
    print(f"This solves the puzzle of day 3, part {'1' if digits == 2 else '2'}!")


if __name__ == "__main__":
    # Set paths
    directory_path: str = os.path.dirname(__file__)
    INPUT_PATH: str = os.path.join(directory_path, "./input.txt")

    print("All printed examples are for the first 5 input values")

    # Get input
    input: list[int] = read_input(path=INPUT_PATH)

    # Turn banks into list of digits
    banks_list: list[list[int]] = [turn_bank_into_list(bank=bank) for bank in input]

    # Day 03, part 01: max joltages per bank (2 digits)
    sum_max_joltages(banks_list=banks_list, digits=2)

    # Day 03, part 02: max joltages per bank (12 digits)
    sum_max_joltages(banks_list=banks_list, digits=12)
