import random
import numpy as np
from typing import List, Tuple

def get_inversions(state: Tuple[int, ...]) -> int:
    """
    Calculate the number of inversions in the puzzle state.
    An inversion is when a tile precedes another tile with a lower number.
    """
    inversions = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] != 0 and state[j] != 0 and state[i] > state[j]:
                inversions += 1
    return inversions

def is_solvable(state: Tuple[int, ...]) -> bool:
    """
    Check if the given 8-puzzle state is solvable.
    A state is solvable if the number of inversions is even.
    """
    return get_inversions(state) % 2 == 0

def generate_8puzzle_instance() -> Tuple[int, ...]:
    """
    Generate a random, solvable 8-puzzle instance.
    Returns a tuple representing the puzzle state where 0 represents the blank space.
    """
    while True:
        # Generate a random permutation of numbers 0-8
        state = list(range(9))
        random.shuffle(state)
        state = tuple(state)
        
        # Check if the generated state is solvable
        if is_solvable(state):
            return state

def get_manhattan_distance(state: Tuple[int, ...], goal: Tuple[int, ...] = (0, 1, 2, 3, 4, 5, 6, 7, 8)) -> int:
    """
    Calculate the Manhattan distance heuristic for the given state.
    """
    distance = 0
    size = 3  # Size of the puzzle grid
    
    for i in range(9):
        if state[i] != 0:  # Skip the blank tile
            current_row = i // size
            current_col = i % size
            
            # Find the goal position of the current number
            goal_idx = goal.index(state[i])
            goal_row = goal_idx // size
            goal_col = goal_idx % size
            
            # Add the Manhattan distance for this tile
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
            
    return distance

def get_blank_position(state: Tuple[int, ...]) -> int:
    """Return the index of the blank (0) in the state."""
    return state.index(0)

def get_valid_moves(blank_pos: int) -> List[str]:
    """
    Get valid moves for the blank tile given its position.
    Returns a list of valid moves: 'up', 'down', 'left', 'right'
    """
    valid_moves = []
    if blank_pos >= 3:  # Can move up
        valid_moves.append('up')
    if blank_pos < 6:  # Can move down
        valid_moves.append('down')
    if blank_pos % 3 != 0:  # Can move left
        valid_moves.append('left')
    if blank_pos % 3 != 2:  # Can move right
        valid_moves.append('right')
    return valid_moves

def apply_move(state: Tuple[int, ...], move: str) -> Tuple[int, ...]:
    """
    Apply the given move to the state and return the new state.
    """
    blank_pos = get_blank_position(state)
    state_list = list(state)
    
    if move == 'up':
        new_pos = blank_pos - 3
    elif move == 'down':
        new_pos = blank_pos + 3
    elif move == 'left':
        new_pos = blank_pos - 1
    elif move == 'right':
        new_pos = blank_pos + 1
    else:
        raise ValueError(f"Invalid move: {move}")
    
    # Swap blank with the tile in the new position
    state_list[blank_pos], state_list[new_pos] = state_list[new_pos], state_list[blank_pos]
    return tuple(state_list)

def print_state(state: Tuple[int, ...]) -> None:
    """Print the puzzle state in a grid format."""
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print() 