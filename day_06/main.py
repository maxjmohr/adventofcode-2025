import os


def read_input(path: str) -> list[list[str]]:
    """Function to read txt as list of strings"""
    with open(path, "r") as file:
        lines: list[list[str]] = [line.strip().split() for line in file.readlines()]

    # Print first 5 lines
    print(f"Input values: {lines[:5]}")
    return lines


def read_input_with_empty_spaces(path: str) -> list[list[str]]:
    """Function to read txt as list of characters of strings"""
    # For each string, really split into single characters
    with open(path, "r") as file:
        lines = [line.rstrip("\n") for line in file]

    # Now split each line into single characters, but keep the spaces as they are important for part 2
    lines_chars: list[list[str]] = [list(line) for line in lines]

    # For each row, print number of columns and the row itself
    # for row in lines_chars:
    # print(f"Number of columns: {len(row)}")

    # Print first 5 lines
    print(f"Input values: {lines_chars[:5]}")
    return lines_chars


def turn_spaces_into_symbols(input: list[list[str]]) -> list[list[str]]:
    """Turn all following spaces in the last row of a symbol into the same symbol (so + or *) until the next symbol is reached, and turn all other spaces into empty strings"""
    last_row = input[-1]
    new_last_row = []
    current_symbol = ""

    for char in last_row:
        if char in ["+", "*"]:
            current_symbol = char
            new_last_row.append(char)
        elif char == " ":
            new_last_row.append(current_symbol if current_symbol else " ")
        else:
            new_last_row.append(char)

    input[-1] = new_last_row
    return input


def turn_vertical_into_numbers(input: list[list[str]]):
    """Turn all lines except the last one of the input into a number by concatenating the characters and turning them into an int, and keep the last line as a symbol
    Example: [[' ', '5', ' ', ' ', '7'], ['1', '2', '6', ' ', ' '], ['2', '4', ' ', ' ', '1'], ['+', '+', '+', ' ', '*']] -> plus_list = [' 12', '524', ' 6 '], product_list=['7 1'] -> plus_list = ['12', '524', '6'], product_list=['71']"""
    plus_list: list[str] = []
    product_list: list[str] = []

    # First pivot the list so you get e.g. from the first row of the example as output:
    # [' ', '1', '2', '+']
    pivoted: list[list[str]] = pivot_list(input=input)
    return pivoted


def pivot_list(input: list[list[str]]) -> list[list[str]]:
    """Function to pivot the columns of the list into rows , with symbol becoming last value"""
    # Get number of cols to loop through
    n_cols: int = len(input[0])

    # Pivot
    return [[row[i] for row in input] for i in range(n_cols)]


def operation_list(list: list[str]) -> int:
    """Function to do the operation of the list based on the symbol (last string)"""
    symbol: str = list[-1]
    numbers: list[int] = [int(value) for value in list[:-1]]

    if symbol == "+":
        return sum(numbers)
    elif symbol == "*":
        result: int = 1
        for number in numbers:
            result *= number
        return result
    else:
        raise ValueError(f"Unknown symbol: {symbol}")


def divide_into_lists(input: list[list[str]]) -> tuple[list[str], list[str]]:
    """Divide the input into two lists, one for the plus symbol and one for the product symbol, by looking at the last row of the input"""
    plus_list: list[str] = []
    product_list: list[str] = []

    for i in range(len(input[0])):
        if input[-1][i] == "+":
            plus_list.append("".join(input[j][i] for j in range(len(input) - 1)))
        elif input[-1][i] == "*":
            product_list.append("".join(input[j][i] for j in range(len(input) - 1)))

    # Delete all empty strings
    plus_list = [value for value in plus_list if value.strip() != ""]
    product_list = [value for value in product_list if value.strip() != ""]

    return plus_list, product_list


if __name__ == "__main__":
    # Set paths
    directory_path: str = os.path.dirname(__file__)
    INPUT_PATH: str = os.path.join(directory_path, "./input.txt")

    print("All printed examples are for the first 5 input values")

    # Get input
    input: list[list[str]] = read_input(path=INPUT_PATH)

    # Pivot list
    pivoted_input: list[list[str]] = pivot_list(input=input)
    print(f"Pivoted input values: {pivoted_input[:5]}")

    # Calculate the operation for each pivoted list and sum them up
    summed_up_problems: int = sum(
        operation_list(list=pivoted_list) for pivoted_list in pivoted_input
    )
    print()
    print(f"Summed up problems to \033[1m{summed_up_problems}\033[0m")
    print("This solves the puzzle of day 6, part 1!")

    # Get input with spaces
    input_with_spaces: list[list[str]] = read_input_with_empty_spaces(path=INPUT_PATH)

    # Turn spaces into symbols
    input_with_spaces: list[list[str]] = turn_spaces_into_symbols(
        input=input_with_spaces
    )
    print(f"Input values with spaces turned into symbols: {input_with_spaces[:5]}")

    # Pivot list
    pivoted_input_2: list[list[str]] = pivot_list(input=input_with_spaces)
    print(f"Pivoted input values: {pivoted_input_2[:5]}")

    # Divide into lists
    plus_list, product_list = divide_into_lists(input=input_with_spaces)
    print(f"Plus list: {plus_list[:5]}")
    print(f"Product list: {product_list[:5]}")

    # Sum up the operations for the plus list and the product list separately and then sum them up
    # Both are list[str]
    plus_list_int: list[int] = [int(value) for value in plus_list]
    summed_plus_list: int = sum(plus_list_int)

    product_list_int: list[int] = [int(value) for value in product_list]
    product_product_list: int = 1
    for value in product_list_int:
        product_product_list *= value

    summed_up_problems: int = summed_plus_list + product_product_list

    print()
    print(f"Summed up problems to \033[1m{'I give up'}\033[0m")
    print("This solves the puzzle of day 6, part 2!")
