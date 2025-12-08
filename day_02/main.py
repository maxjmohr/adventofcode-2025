import os


def read_input(path: str) -> list[str]:
    """Function to read txt as list of strings"""
    with open(path, "r") as file:
        line: str = file.read().strip()

    lines: list[str] = line.split(",")

    # Print first 5 lines
    print(f"Input values: {lines[:5]}")
    return lines


def transform_range_into_ids(range_str: str) -> list[int]:
    """Transform a range e.g. 11-13 into a list of the ids [11, 12, 13]"""
    start_str, end_str = range_str.split("-")
    start: int = int(start_str)
    end: int = int(end_str)

    ids: list[int] = list(range(start, end + 1))
    return ids


def create_all_ids(ranges: list[str]) -> list[int]:
    """From the input ranges create a list of all possible ids"""
    all_ids: list[int] = [i for r in ranges for i in transform_range_into_ids(r)]

    print(f"First 5 IDs: {all_ids[:5]}")
    return all_ids


def invalid_id_part1(id: int) -> int:
    """If invalid id, return id, else 0
    - must be round digits so 2,4,6,... digit numbers
    - dividing the ids in half, first and second half must be identical
    """
    id_str: str = str(id)
    length: int = len(id_str)

    # Check if length is even, else valid = 0
    if length % 2 != 0:
        return 0

    # Split in half
    half: int = length // 2
    first_half: str = id_str[:half]
    second_half: str = id_str[half:]

    # Check if first half == second half, else valid = 0
    if first_half != second_half:
        return 0

    return id


def invalid_id_part2(id: int) -> int:
    """If invalid id, return id, else
    for each id:
    - check if dividable by 2 (without remainder)
      if yes: dividing the id in half, first and second half must be identical
    - if not identical, check if dividable by 3 (without remainder)
      if yes divide into 3 parts, all three must be identical
    ... until the length of the id
    """
    id_str: str = str(id)
    length: int = len(id_str)

    # Minimum 2 parts, maximum length of id
    for divisor in range(2, length + 1):
        # Only if dividable into equal parts
        if length % divisor == 0:
            part_length: int = length // divisor
            parts: list[str] = [
                id_str[i * part_length : (i + 1) * part_length] for i in range(divisor)
            ]

            # Check if all parts are identical
            if all(part == parts[0] for part in parts):
                return id  # Inalid ID

    return 0  # Valid ID


def sum_invalid_ids(all_ids: list[int], part: int) -> None:
    """Sum invalid ids
    - must be round digits so 2,4,6,... digit numbers
    - dividing the ids in half, first and second half must be identical
    """
    if part == 1:
        # Turn all valid ids to 0 and keep invalid as is
        invalid_ids: list[int] = [invalid_id_part1(id) for id in all_ids]
        print(f"First 5 IDs after check: {invalid_ids[:5]}")

        # Sum all invalid ids
        result: int = sum(invalid_ids)

        print()
        print(f"Summed up invalid IDs to \033[1m{result}\033[0m")
        print("This solves the puzzle of day 2, part 1!")

    elif part == 2:
        # Turn all valid ids to 0 and keep invalid as is
        invalid_ids: list[int] = [invalid_id_part2(id) for id in all_ids]
        print(f"First 5 IDs after check: {invalid_ids[:5]}")

        # Sum all invalid ids
        result: int = sum(invalid_ids)

        print()
        print(f"Summed up invalid IDs to \033[1m{result}\033[0m")
        print("This solves the puzzle of day 2, part 2!")


if __name__ == "__main__":
    # Set paths
    directory_path: str = os.path.dirname(__file__)
    INPUT_PATH: str = os.path.join(directory_path, "./input.txt")

    print("All printed examples are for the first 5 input values")

    # Get input
    input: list[str] = read_input(path=INPUT_PATH)

    # Turn ranges into long list of all possible ids
    all_ids: list[int] = create_all_ids(ranges=input)

    # Sum invalid ids (part 1)
    sum_invalid_ids(all_ids=all_ids, part=1)
    print()

    # Sum invalid ids (part 2)
    sum_invalid_ids(all_ids=all_ids, part=2)
