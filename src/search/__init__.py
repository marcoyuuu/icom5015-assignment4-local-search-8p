"""
Search algorithms module.
Contains implementations of A* search and other search algorithms.
"""

from .astar_search import astar_search, PuzzleState, generate_solvable_puzzle

__all__ = ['astar_search', 'PuzzleState', 'generate_solvable_puzzle'] 