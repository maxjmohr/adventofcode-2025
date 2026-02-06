import os


def read_input(path: str) -> list[str]:
    """Function to read txt as list of strings"""
    with open(path, "r") as file:
        lines: list[str] = [line.strip() for line in file.readlines()]

    # Print first 5 lines
    print(f"Input values: {lines[:5]}")
    return lines


def turn_row_into_list(row: str) -> list[int]:
    """Turn long sequence (row) into list of single digits"""
    return [0 if character == "." else 1 for character in str(row)]


def get_removable_papers_once(rows_list: list[list[int]]) -> int:
    """We loop through each value of rows_list
    If this value is 0, we don't add a row to the results
    If it is 1, we get all neighbors (so 8 values around target, less if it is at a border) and add them as a row to the results
    If the sum of the neighbors (excluding target) < 4, then add 1 to the count of papers removable by the forklift
    """
    removable_papers: int = 0
    n_rows: int = len(rows_list)
    n_cols: int = len(rows_list[0])

    # Loop through rows
    for i in range(n_rows):
        # Now in the row, loop through each value as target
        for j in range(n_cols):
            # Only if the value itself is a paper roll (1), get neighbors
            if rows_list[i][j] == 1:
                neighbors: list[int] = []
                # Get the relative indices
                for i_search in [-1, 0, 1]:
                    for j_search in [-1, 0, 1]:
                        # Skip target itself
                        if i_search == 0 and j_search == 0:
                            continue
                        # Get the actual neighboring indices
                        i_neighbor, j_neighbor = i + i_search, j + j_search
                        if 0 <= i_neighbor < n_rows and 0 <= j_neighbor < n_cols:
                            neighbors.append(rows_list[i_neighbor][j_neighbor])
                if sum(neighbors) < 4:
                    removable_papers += 1

    return removable_papers


def get_removable_papers_repeatadly(rows_list: list[list[int]]) -> int:
    """We loop through each value of rows_list
    If this value is 0, we don't add a row to the results
    If it is 1, we get all neighbors (so 8 values around target, less if it is at a border) and add them as a row to the results
    If the sum of the neighbors (excluding target) < 4, then add 1 to the count of papers removable by the forklift
    As soon as you have checked whether the papers can be removed and have removed them, repeat the process until there are no more papers that can be removed
    """
    removable_papers: int = 0
    removable_papers_indices: list[tuple[int, int]] = []
    removed_papers_in_last_iteration: bool = True

    while removed_papers_in_last_iteration:
        # Get dimensions
        n_rows: int = len(rows_list)
        n_cols: int = len(rows_list[0])

        # Set removed papers to False
        removed_papers_in_last_iteration = False

        # Loop through rows
        for i in range(n_rows):
            # Now in the row, loop through each value as target
            for j in range(n_cols):
                # Only if the value itself is a paper roll (1), get neighbors
                if rows_list[i][j] == 1:
                    neighbors: list[int] = []
                    # Get the relative indices
                    for i_search in [-1, 0, 1]:
                        for j_search in [-1, 0, 1]:
                            # Skip target itself
                            if i_search == 0 and j_search == 0:
                                continue
                            # Get the actual neighboring indices
                            i_neighbor, j_neighbor = i + i_search, j + j_search
                            if 0 <= i_neighbor < n_rows and 0 <= j_neighbor < n_cols:
                                neighbors.append(rows_list[i_neighbor][j_neighbor])

                    # Can remove paper if less than 4 papers as neighbors
                    if sum(neighbors) < 4:
                        removable_papers += 1
                        # Make sure to remove paper for next iteration
                        removable_papers_indices.append((i, j))

        # Remove papers
        if removable_papers_indices != []:
            removed_papers_in_last_iteration = True
            # Remove all papers that were marked for removal
            for i, j in removable_papers_indices:
                rows_list[i][j] = 0
            # Clear the list for next iteration
            removable_papers_indices = []

        # Check if an entire row is empty, if so, remove it
        rows_list = [row for row in rows_list if any(value == 1 for value in row)]

    return removable_papers


if __name__ == "__main__":
    # Set paths
    directory_path: str = os.path.dirname(__file__)
    INPUT_PATH: str = os.path.join(directory_path, "./input.txt")

    print("All printed examples are for the first 5 input values")

    # Get input
    input: list[str] = read_input(path=INPUT_PATH)

    # Turn banks into list of digits
    rows_list: list[list[int]] = [turn_row_into_list(row=row) for row in input]
    print(f"Input values as list: {rows_list[:5]}")

    # Get neighbors and count accessible papers once
    removable_papers: int = get_removable_papers_once(rows_list=rows_list)
    print()
    print(f"Summed up removable papers to \033[1m{removable_papers}\033[0m")
    print("This solves the puzzle of day 4, part 1!")

    # Get neighbors and count accessible papers repeatedly
    removable_papers_repeatedly: int = get_removable_papers_repeatadly(
        rows_list=rows_list
    )
    print()
    print(f"Summed up removable papers to \033[1m{removable_papers_repeatedly}\033[0m")
    print("This solves the puzzle of day 4, part 2!")
