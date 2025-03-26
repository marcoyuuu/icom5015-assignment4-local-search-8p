from heapq import heappush, heappop
import numpy as np
from typing import List, Tuple, Optional

class PuzzleState:
    def __init__(self, board: List[int], parent=None, action=None, path_cost=0):
        self.board = board
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.blank_pos = board.index(0)
    
    def get_neighbors(self) -> List[Tuple[List[int], str]]:
        """Get all possible next states."""
        neighbors = []
        blank_row, blank_col = self.blank_pos // 3, self.blank_pos % 3
        
        # Possible moves: up, down, left, right
        moves = [
            (-1, 0, 'up'), (1, 0, 'down'),
            (0, -1, 'left'), (0, 1, 'right')
        ]
        
        for dr, dc, action in moves:
            new_row, new_col = blank_row + dr, blank_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_pos = new_row * 3 + new_col
                new_board = self.board.copy()
                new_board[self.blank_pos], new_board[new_pos] = new_board[new_pos], new_board[self.blank_pos]
                neighbors.append((new_board, action))
        
        return neighbors
    
    def manhattan_distance(self) -> int:
        """Calculate Manhattan distance heuristic."""
        distance = 0
        for i in range(9):
            if self.board[i] != 0:  # Skip blank
                curr_row, curr_col = i // 3, i % 3
                goal_row, goal_col = self.board[i] // 3, self.board[i] % 3
                distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
        return distance
    
    def is_goal(self) -> bool:
        """Check if current state is goal state."""
        return self.board == list(range(9))
    
    def path(self) -> List[str]:
        """Return path of actions from start to current state."""
        actions = []
        current = self
        while current.parent:
            actions.append(current.action)
            current = current.parent
        return list(reversed(actions))

def astar_search(initial_state: PuzzleState) -> Optional[PuzzleState]:
    """A* search algorithm."""
    frontier = []  # Priority queue
    explored = set()
    
    # Add initial state to frontier
    heappush(frontier, (initial_state.manhattan_distance(), id(initial_state), initial_state))
    
    while frontier:
        _, _, current = heappop(frontier)
        
        if current.is_goal():
            return current
        
        board_tuple = tuple(current.board)
        if board_tuple in explored:
            continue
            
        explored.add(board_tuple)
        
        for next_board, action in current.get_neighbors():
            if tuple(next_board) not in explored:
                child = PuzzleState(
                    next_board,
                    parent=current,
                    action=action,
                    path_cost=current.path_cost + 1
                )
                f = child.path_cost + child.manhattan_distance()
                heappush(frontier, (f, id(child), child))
    
    return None  # No solution found

def generate_solvable_puzzle() -> List[int]:
    """Generate a random solvable 8-puzzle instance."""
    while True:
        puzzle = list(range(9))
        np.random.shuffle(puzzle)
        # Check if puzzle is solvable
        inversions = sum(1 for i in range(9) for j in range(i + 1, 9)
                        if puzzle[i] != 0 and puzzle[j] != 0 and puzzle[i] > puzzle[j])
        if inversions % 2 == 0:  # Puzzle is solvable
            return puzzle 