import random
import math
from typing import Callable, TypeVar, List, Tuple, Any

State = TypeVar('State')

def hill_climbing_steepest(
    initial_state: State,
    get_neighbors: Callable[[State], List[State]],
    evaluate: Callable[[State], float],
    max_iterations: int = 1000
) -> Tuple[State, List[float]]:
    """
    Steepest-ascent hill climbing algorithm.
    Returns the best state found and the history of values.
    """
    current = initial_state
    current_value = evaluate(current)
    value_history = [current_value]
    
    for _ in range(max_iterations):
        neighbors = get_neighbors(current)
        if not neighbors:
            break
            
        # Find the neighbor with the highest value
        neighbor_values = [(n, evaluate(n)) for n in neighbors]
        best_neighbor, best_value = max(neighbor_values, key=lambda x: x[1])
        
        if best_value <= current_value:
            break
            
        current = best_neighbor
        current_value = best_value
        value_history.append(current_value)
    
    return current, value_history

def hill_climbing_first_choice(
    initial_state: State,
    get_neighbors: Callable[[State], List[State]],
    evaluate: Callable[[State], float],
    max_iterations: int = 1000
) -> Tuple[State, List[float]]:
    """
    First-choice hill climbing algorithm.
    Returns the best state found and the history of values.
    """
    current = initial_state
    current_value = evaluate(current)
    value_history = [current_value]
    
    for _ in range(max_iterations):
        neighbors = get_neighbors(current)
        if not neighbors:
            break
            
        # Shuffle neighbors to randomize the search
        random.shuffle(neighbors)
        
        # Find first neighbor that improves the value
        found_better = False
        for neighbor in neighbors:
            neighbor_value = evaluate(neighbor)
            if neighbor_value > current_value:
                current = neighbor
                current_value = neighbor_value
                value_history.append(current_value)
                found_better = True
                break
                
        if not found_better:
            break
    
    return current, value_history

def hill_climbing_random_restart(
    initial_state: State,
    get_neighbors: Callable[[State], List[State]],
    evaluate: Callable[[State], float],
    generate_state: Callable[[], State],
    max_restarts: int = 10,
    max_iterations: int = 1000
) -> Tuple[State, List[float]]:
    """
    Random-restart hill climbing algorithm.
    Returns the best state found across all restarts and the history of values.
    """
    best_state = initial_state
    best_value = evaluate(best_state)
    value_history = [best_value]
    
    for _ in range(max_restarts):
        current_state = generate_state()
        current_state, current_history = hill_climbing_steepest(
            current_state,
            get_neighbors,
            evaluate,
            max_iterations
        )
        current_value = evaluate(current_state)
        value_history.extend(current_history)
        
        if current_value > best_value:
            best_state = current_state
            best_value = current_value
    
    return best_state, value_history

def simulated_annealing(
    initial_state: State,
    get_neighbors: Callable[[State], List[State]],
    evaluate: Callable[[State], float],
    temperature_schedule: Callable[[int], float],
    max_iterations: int = 1000
) -> Tuple[State, List[float]]:
    """
    Simulated annealing algorithm.
    Returns the best state found and the history of values.
    """
    current = initial_state
    current_value = evaluate(current)
    best_state = current
    best_value = current_value
    value_history = [current_value]
    
    for t in range(max_iterations):
        temperature = temperature_schedule(t)
        if temperature == 0:
            break
            
        neighbors = get_neighbors(current)
        if not neighbors:
            break
            
        next_state = random.choice(neighbors)
        next_value = evaluate(next_state)
        
        # Calculate change in value
        delta_e = next_value - current_value
        
        # Accept if better or with probability based on temperature
        if delta_e > 0 or random.random() < math.exp(delta_e / temperature):
            current = next_state
            current_value = next_value
            value_history.append(current_value)
            
            # Update best state if current is better
            if current_value > best_value:
                best_state = current
                best_value = current_value
    
    return best_state, value_history

def exponential_schedule(k: float = 20, lam: float = 0.005, limit: int = 1000) -> Callable[[int], float]:
    """
    Creates an exponential cooling schedule for simulated annealing.
    """
    return lambda t: k * math.exp(-lam * t) if t < limit else 0 