import random
import math
from typing import List, Tuple, Callable, Any

def hill_climbing_steepest(
    initial_state: List[int],
    get_neighbors: Callable[[List[int]], List[List[int]]],
    evaluate: Callable[[List[int]], float]
) -> Tuple[List[int], List[float]]:
    """
    Steepest-ascent hill climbing implementation.
    """
    current_state = initial_state
    current_value = evaluate(current_state)
    value_history = [current_value]
    
    while True:
        neighbors = get_neighbors(current_state)
        if not neighbors:
            break
            
        # Find the best neighbor
        best_neighbor = max(neighbors, key=evaluate)
        best_value = evaluate(best_neighbor)
        
        if best_value <= current_value:
            break
            
        current_state = best_neighbor
        current_value = best_value
        value_history.append(current_value)
    
    return current_state, value_history

def hill_climbing_first_choice(
    initial_state: List[int],
    get_neighbors: Callable[[List[int]], List[List[int]]],
    evaluate: Callable[[List[int]], float]
) -> Tuple[List[int], List[float]]:
    """
    First-choice hill climbing implementation.
    """
    current_state = initial_state
    current_value = evaluate(current_state)
    value_history = [current_value]
    
    while True:
        neighbors = get_neighbors(current_state)
        if not neighbors:
            break
            
        # Randomly shuffle neighbors
        random.shuffle(neighbors)
        
        # Find first improving neighbor
        improved = False
        for neighbor in neighbors:
            neighbor_value = evaluate(neighbor)
            if neighbor_value > current_value:
                current_state = neighbor
                current_value = neighbor_value
                value_history.append(current_value)
                improved = True
                break
                
        if not improved:
            break
    
    return current_state, value_history

def hill_climbing_random_restart(
    initial_state: List[int],
    get_neighbors: Callable[[List[int]], List[List[int]]],
    evaluate: Callable[[List[int]], float],
    generate_random_state: Callable[[], List[int]],
    max_restarts: int = 10
) -> Tuple[List[int], List[float]]:
    """
    Random restart hill climbing implementation.
    """
    best_state = initial_state
    best_value = evaluate(initial_state)
    all_value_history = []
    
    for _ in range(max_restarts):
        current_state = generate_random_state()
        current_value = evaluate(current_state)
        value_history = [current_value]
        
        while True:
            neighbors = get_neighbors(current_state)
            if not neighbors:
                break
                
            # Find the best neighbor
            best_neighbor = max(neighbors, key=evaluate)
            best_neighbor_value = evaluate(best_neighbor)
            
            if best_neighbor_value <= current_value:
                break
                
            current_state = best_neighbor
            current_value = best_neighbor_value
            value_history.append(current_value)
        
        all_value_history.extend(value_history)
        
        if current_value > best_value:
            best_state = current_state
            best_value = current_value
    
    return best_state, all_value_history

def simulated_annealing(
    initial_state: List[int],
    get_neighbors: Callable[[List[int]], List[List[int]]],
    evaluate: Callable[[List[int]], float],
    schedule: Callable[[int], float]
) -> Tuple[List[int], List[float]]:
    """
    Simulated annealing implementation.
    """
    current_state = initial_state
    current_value = evaluate(current_state)
    value_history = [current_value]
    
    for t in range(1, 1000):  # Max 1000 iterations
        temperature = schedule(t)
        if temperature <= 0:
            break
            
        neighbors = get_neighbors(current_state)
        if not neighbors:
            break
            
        # Randomly select a neighbor
        next_state = random.choice(neighbors)
        next_value = evaluate(next_state)
        
        # Calculate delta E (negative because we're maximizing)
        delta_e = next_value - current_value
        
        # Accept worse solutions with probability based on temperature
        if delta_e > 0 or random.random() < math.exp(delta_e / temperature):
            current_state = next_state
            current_value = next_value
            value_history.append(current_value)
    
    return current_state, value_history

def exponential_schedule(k: float = 20, lam: float = 0.005) -> Callable[[int], float]:
    """
    Exponential cooling schedule for simulated annealing.
    """
    return lambda t: k * math.exp(-lam * t)

def linear_schedule(t: int, max_t: int = 1000) -> float:
    """
    Linear cooling schedule for simulated annealing.
    """
    return max(0.01, (1 - t / max_t)) 