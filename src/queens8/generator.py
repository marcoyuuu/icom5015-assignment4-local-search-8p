import random
from typing import List, Tuple

def generate_8queens_state() -> Tuple[int, ...]:
    """
    Generate a random 8-queens state where each queen is placed in a different column.
    Returns a tuple where the index represents the column and the value represents the row.
    """
    # Generate a random permutation of rows (0-7)
    state = list(range(8))
    random.shuffle(state)
    return tuple(state)

def count_conflicts(state: Tuple[int, ...]) -> int:
    """
    Count the number of conflicts (attacking pairs) in the current state.
    A conflict occurs when two queens can attack each other.
    """
    conflicts = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j]:  # Same row
                conflicts += 1
            elif abs(i - j) == abs(state[i] - state[j]):  # Same diagonal
                conflicts += 1
    return conflicts

def get_neighbors(state: Tuple[int, ...]) -> List[Tuple[int, ...]]:
    """
    Generate all possible neighbor states by moving one queen to a different row in its column.
    """
    neighbors = []
    for col in range(len(state)):
        for row in range(len(state)):
            if row != state[col]:
                new_state = list(state)
                new_state[col] = row
                neighbors.append(tuple(new_state))
    return neighbors

def print_board(state: Tuple[int, ...]) -> None:
    """
    Print the chess board with queens placed according to the state.
    """
    for row in range(len(state)):
        line = ""
        for col in range(len(state)):
            if state[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def is_solution(state: Tuple[int, ...]) -> bool:
    """
    Check if the current state is a solution (no conflicts).
    """
    return count_conflicts(state) == 0 