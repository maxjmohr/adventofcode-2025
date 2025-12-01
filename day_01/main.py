import os
from itertools import accumulate


def read_input(path: str) -> list[str]:
    """Function to read txt as list of strings"""
    with open(path, "r") as file:
        lines: list[str] = [line.strip() for line in file.readlines()]

    # Print first 5 lines
    print(f"Input values: {lines[:5]}")
    return lines


def turn_letter_to_sign(letter: str) -> int:
    """Function to turn 'L' to -1 and 'R' to 1"""
    if letter == "L":
        return -1
    else:
        return 1


def split_and_turn_into_steps(instruction: str) -> int:
    """Function to turn string into letter and integer e.g. 'L10' -> ('L', 10)"""
    # Get first letter and turn into sign
    sign: int = turn_letter_to_sign(instruction[0])

    # Get and minimize the steps
    steps: int = int(instruction[1:])

    return sign * steps


def add_initial_value(start: int, steps: list[int]) -> list[int]:
    """Function to add initial value to the beginning"""
    print(f"Adding starting value {start} to list")
    return [start] + steps


def recursively_sumup(steps: list[int]) -> list[int]:
    """Use the steps to recursively sumup them
    Later on, we can check which steps are at 0 or dividable by 100 to get the result
    So e.g. [50, 100, -20 -80, -50] will become [50, 150, 130, 50, 0]
    """
    return list(accumulate(steps))


def count_0_or_dividable_by_100(summed_steps: list[int]) -> int:
    """Function to count how many times we land on 0 or a number dividable by 100"""
    count: int = 0

    # Check if we landed on 0 or dividable by 100
    for step in summed_steps:
        if step % 100 == 0:
            count += 1
    print()
    print(f"Counted \033[1m{count} times\033[0m that are 0 or dividable by 100.")
    print("This solves the puzzle of day 1, part 1!")
    return count


def count_0_or_dividable_by_100_or_jumped_over(summed_steps: list[int]) -> int:
    """Function to count how many times we land on 0 or a number dividable by 100 but now including jumps over such numbers"""
    count: int = 0
    previous_step: int = summed_steps[0]

    for current_step in summed_steps:
        # Check if we landed on 0 or dividable by 100
        if current_step % 100 == 0:
            count += 1

        # Check if we jumped over a number dividable by 100
        lower_bound: int = min(previous_step, current_step)
        upper_bound: int = max(previous_step, current_step)

        for number in range(lower_bound + 1, upper_bound):
            if number % 100 == 0:
                count += 1

        previous_step = current_step

    print()
    print(
        f"Counted \033[1m{count} times\033[0m that are 0 or dividable by 100 or jumped over."
    )
    print("This solves the puzzle of day 1, part 2!")
    return count


if __name__ == "__main__":
    # Set paths
    directory_path: str = os.path.dirname(__file__)
    INPUT_PATH: str = os.path.join(directory_path, "./input.txt")

    # Set starting value
    STARTING_VALUE: int = 50

    print("All printed examples are for the first 5 input values")

    # Get input
    input: list[str] = read_input(path=INPUT_PATH)

    # Split instructions into letter and integer
    steps: list[int] = [split_and_turn_into_steps(instruction=i) for i in input]
    print(f"Steps: {steps[:5]}")

    # Add starting point to list beginning
    total_steps: list[int] = add_initial_value(start=STARTING_VALUE, steps=steps)
    print(f"Total steps: {total_steps[:5]}")

    # Recursively sumup the steps
    summed_steps: list[int] = recursively_sumup(steps=total_steps)
    print(f"Summed steps: {summed_steps[:5]}")

    # Count how many times we land on 0 or a number dividable by 100
    result_part_1: int = count_0_or_dividable_by_100(summed_steps=summed_steps)

    # Count how many times we land on 0 or a number dividable by 100 or jumped over
    result_part_2: int = count_0_or_dividable_by_100_or_jumped_over(
        summed_steps=summed_steps
    )
