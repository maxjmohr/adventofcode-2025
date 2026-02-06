import os


def read_input(path: str) -> tuple[list[str], list[int]]:
    """Function to read txt as list of strings"""
    # Read as two lists
    # ranges includes all lines with - in the string
    with open(path, "r") as file:
        ranges: list[str] = [line.strip() for line in file.readlines() if "-" in line]

    # ids includes all other rows that are not empty
    with open(path, "r") as file:
        available_ids: list[int] = [
            int(line.strip())
            for line in file.readlines()
            if line.strip() and "-" not in line
        ]

    # Print first 5 lines
    print(f"Input values (ranges): {ranges[:5]}")
    print(f"Input values (available ids): {available_ids[:5]}")
    return ranges, available_ids


# Inital though (as day_02, but too imperformant)
def transform_range_into_ids(range_str: str) -> list[int]:
    """Transform a range e.g. 11-13 into a list of the ids [11, 12, 13]"""
    start_str, end_str = range_str.split("-")
    start: int = int(start_str)
    end: int = int(end_str)

    ids: list[int] = list(range(start, end + 1))
    return ids


def transform_range_into_edge_ids(range_str: str) -> list[int]:
    """Transform a range e.g. 11-13 into a list of the edge ids [11, 13]"""
    start_str, end_str = range_str.split("-")
    start: int = int(start_str)
    end: int = int(end_str)
    return [start, end]


def create_edge_fresh_ids(ranges: list[str]) -> list[list[int]]:
    """From the input ranges create a list of all edge ids"""
    all_ids: list[list[int]] = [transform_range_into_edge_ids(r) for r in ranges]

    print(f"Input values (fresh edge ids): {all_ids[:5]}")
    return all_ids


def check_if_in_range(available_id: int, fresh_ids_edges: list[list[int]]) -> int:
    """Check if the available id is in any of the ranges
    If yes, return 1, else 0
    """
    for edge_ids in fresh_ids_edges:
        if edge_ids[0] <= available_id <= edge_ids[1]:
            return 1
    return 0


def count_available_fresh_ids(available_fresh_ids: list[int]) -> None:
    """Sum the list of available fresh ids to get the total count"""
    count: int = sum(available_fresh_ids)
    print()
    print(f"Summed up available and fresh ids to \033[1m{count}\033[0m")
    print("This solves the puzzle of day 5, part 1!")


def count_all_fresh_ids(fresh_ids_edges: list[list[int]]) -> None:
    """Count all fresh ids
    As we cant just create all ids from ranges and count them, we have to merge the ranges together first
    So we first order the id edges from bottom to top by their start value
    Then we loop through each edges and if the bottom edge of the next edge is <= to the top edge prior, we extend the top edge by the max of both top edges
    """
    # Sort the id edges by starting point
    fresh_ids_edges.sort(key=lambda x: x[0])

    # Initialize merged ranges with the first range
    merged_ranges: list[list[int]] = [fresh_ids_edges[0]]

    # Get target edges
    for bottom_edge, top_edge in fresh_ids_edges:
        # Get latest merged ranges
        bottom_merged, top_merged = merged_ranges[-1]

        # If the bottom edge is <= to the prior top edge, we take the max top and merge
        if bottom_edge <= top_merged:
            merged_ranges[-1][1] = max(top_merged, top_edge)
        # Else we append as this is a new range
        else:
            merged_ranges.append([bottom_edge, top_edge])

    # Now count all ids in merged ranges
    total_count: int = sum([top - bottom + 1 for bottom, top in merged_ranges])

    print()
    print(f"Counted all fresh ids to \033[1m{total_count}\033[0m")
    print("This solves the puzzle of day 5, part 2!")


if __name__ == "__main__":
    # Set paths
    directory_path: str = os.path.dirname(__file__)
    INPUT_PATH: str = os.path.join(directory_path, "./input.txt")

    print("All printed examples are for the first 5 input values")

    # Get input
    ranges, available_ids = read_input(path=INPUT_PATH)

    # Get fresh ids
    fresh_ids_edges: list[list[int]] = create_edge_fresh_ids(ranges=ranges)

    # Check which available ids are fresh
    available_fresh_ids: list[int] = [
        check_if_in_range(available_id=id, fresh_ids_edges=fresh_ids_edges)
        for id in available_ids
    ]

    # Count available and fresh ids
    count_available_fresh_ids(available_fresh_ids=available_fresh_ids)

    # Count all fresh ids
    count_all_fresh_ids(fresh_ids_edges=fresh_ids_edges)
