import time
import json
from typing import Dict, List, Any
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

from .ai_berkeley.local_search import (
    hill_climbing_steepest,
    hill_climbing_first_choice,
    hill_climbing_random_restart,
    simulated_annealing,
    exponential_schedule
)

from .ai_berkeley.search import astar_search, EightPuzzle
from .puzzle8.generator import (
    generate_8puzzle_instance,
    get_manhattan_distance,
    get_valid_moves,
    apply_move,
    print_state
)
from .queens8.generator import (
    generate_8queens_state,
    count_conflicts,
    get_neighbors,
    print_board,
    is_solution
)

def run_8puzzle_experiments(num_instances: int = 100) -> pd.DataFrame:
    """
    Run experiments on the 8-puzzle problem using different local search algorithms.
    """
    results = []
    print(f"\nRunning 8-puzzle experiments ({num_instances} instances):")
    
    for i in range(num_instances):
        print(f"\rProgress: {i+1}/{num_instances} instances ({(i+1)/num_instances*100:.1f}%)", end="")
        
        initial_state = generate_8puzzle_instance()
        
        # Get optimal solution cost using A*
        puzzle = EightPuzzle(initial_state)
        astar_result = astar_search(puzzle)
        optimal_cost = astar_result.path_cost if astar_result else float('inf')
        
        # Define evaluation function (negative Manhattan distance as we want to maximize)
        evaluate = lambda state: -get_manhattan_distance(state)
        
        # Run each algorithm and collect metrics
        algorithms = {
            'Hill Climbing (Steepest)': lambda: hill_climbing_steepest(
                initial_state,
                lambda s: [apply_move(s, m) for m in get_valid_moves(s.index(0))],
                evaluate
            ),
            'Hill Climbing (First Choice)': lambda: hill_climbing_first_choice(
                initial_state,
                lambda s: [apply_move(s, m) for m in get_valid_moves(s.index(0))],
                evaluate
            ),
            'Hill Climbing (Random Restart)': lambda: hill_climbing_random_restart(
                initial_state,
                lambda s: [apply_move(s, m) for m in get_valid_moves(s.index(0))],
                evaluate,
                generate_8puzzle_instance
            ),
            'Simulated Annealing': lambda: simulated_annealing(
                initial_state,
                lambda s: [apply_move(s, m) for m in get_valid_moves(s.index(0))],
                evaluate,
                exponential_schedule(k=20, lam=0.005)
            )
        }
        
        for algo_name, algo_func in algorithms.items():
            start_time = time.time()
            final_state, value_history = algo_func()
            runtime = time.time() - start_time
            
            # Calculate additional metrics
            initial_value = evaluate(initial_state)
            final_value = evaluate(final_state)
            improvement = initial_value - final_value
            solution_found = get_manhattan_distance(final_state) == 0
            
            results.append({
                'Problem': '8-Puzzle',
                'Instance': i,
                'Algorithm': algo_name,
                'Initial State': initial_state,
                'Final State': final_state,
                'Initial Value': initial_value,
                'Final Value': final_value,
                'Value Improvement': improvement,
                'Optimal Cost': optimal_cost,
                'Solution Found': solution_found,
                'Steps': len(value_history) - 1,
                'Runtime': runtime,
                'Value History': value_history
            })
    
    print("\nCompleted 8-puzzle experiments.")
    return pd.DataFrame(results)

def run_8queens_experiments(num_instances: int = 100) -> pd.DataFrame:
    """
    Run experiments on the 8-queens problem using different local search algorithms.
    """
    results = []
    print(f"\nRunning 8-queens experiments ({num_instances} instances):")
    
    for i in range(num_instances):
        print(f"\rProgress: {i+1}/{num_instances} instances ({(i+1)/num_instances*100:.1f}%)", end="")
        
        initial_state = generate_8queens_state()
        
        # Define evaluation function (negative conflicts as we want to maximize)
        evaluate = lambda state: -count_conflicts(state)
        
        # Run each algorithm and collect metrics
        algorithms = {
            'Hill Climbing (Steepest)': lambda: hill_climbing_steepest(
                initial_state,
                get_neighbors,
                evaluate
            ),
            'Hill Climbing (First Choice)': lambda: hill_climbing_first_choice(
                initial_state,
                get_neighbors,
                evaluate
            ),
            'Hill Climbing (Random Restart)': lambda: hill_climbing_random_restart(
                initial_state,
                get_neighbors,
                evaluate,
                generate_8queens_state
            ),
            'Simulated Annealing': lambda: simulated_annealing(
                initial_state,
                get_neighbors,
                evaluate,
                exponential_schedule(k=20, lam=0.005)
            )
        }
        
        for algo_name, algo_func in algorithms.items():
            start_time = time.time()
            final_state, value_history = algo_func()
            runtime = time.time() - start_time
            
            # Calculate additional metrics
            initial_value = evaluate(initial_state)
            final_value = evaluate(final_state)
            improvement = initial_value - final_value
            solution_found = is_solution(final_state)
            
            results.append({
                'Problem': '8-Queens',
                'Instance': i,
                'Algorithm': algo_name,
                'Initial State': initial_state,
                'Final State': final_state,
                'Initial Value': initial_value,
                'Final Value': final_value,
                'Value Improvement': improvement,
                'Solution Found': solution_found,
                'Steps': len(value_history) - 1,
                'Runtime': runtime,
                'Value History': value_history
            })
    
    print("\nCompleted 8-queens experiments.")
    return pd.DataFrame(results)

def plot_results(results: pd.DataFrame, output_dir: Path) -> None:
    """
    Create and save professional visualizations of the experimental results.
    """
    # Set style for all plots
    plt.style.use('default')
    
    # Color scheme
    colors = ['#2ecc71', '#3498db', '#e74c3c', '#f1c40f']
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Success rate by algorithm and problem
    plt.figure(figsize=(12, 6))
    success_rates = results.groupby(['Problem', 'Algorithm'])['Solution Found'].mean() * 100
    ax = success_rates.unstack().plot(kind='bar', color=colors)
    plt.title('Success Rate by Algorithm and Problem', pad=20, fontsize=14)
    plt.xlabel('Problem Type', fontsize=12)
    plt.ylabel('Success Rate (%)', fontsize=12)
    plt.xticks(rotation=0)
    plt.legend(title='Algorithm', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Add value labels on top of bars
    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f%%', padding=3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'success_rates.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Average runtime by algorithm and problem
    plt.figure(figsize=(12, 6))
    runtimes = results.groupby(['Problem', 'Algorithm'])['Runtime'].mean()
    ax = runtimes.unstack().plot(kind='bar', color=colors)
    plt.title('Average Runtime by Algorithm and Problem', pad=20, fontsize=14)
    plt.xlabel('Problem Type', fontsize=12)
    plt.ylabel('Runtime (seconds)', fontsize=12)
    plt.xticks(rotation=0)
    plt.legend(title='Algorithm', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Add value labels on top of bars
    for container in ax.containers:
        ax.bar_label(container, fmt='%.2f', padding=3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'runtimes.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Average steps by algorithm and problem
    plt.figure(figsize=(12, 6))
    steps = results.groupby(['Problem', 'Algorithm'])['Steps'].mean()
    ax = steps.unstack().plot(kind='bar', color=colors)
    plt.title('Average Steps by Algorithm and Problem', pad=20, fontsize=14)
    plt.xlabel('Problem Type', fontsize=12)
    plt.ylabel('Number of Steps', fontsize=12)
    plt.xticks(rotation=0)
    plt.legend(title='Algorithm', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Add value labels on top of bars
    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f', padding=3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'steps.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # For 8-puzzle: Plot steps vs optimal cost
    puzzle_results = results[results['Problem'] == '8-Puzzle']
    plt.figure(figsize=(12, 6))
    
    for idx, algo in enumerate(puzzle_results['Algorithm'].unique()):
        algo_data = puzzle_results[puzzle_results['Algorithm'] == algo]
        plt.scatter(algo_data['Optimal Cost'], algo_data['Steps'], 
                   label=algo, alpha=0.6, color=colors[idx], s=100)
        
        # Add trend line
        z = np.polyfit(algo_data['Optimal Cost'], algo_data['Steps'], 1)
        p = np.poly1d(z)
        plt.plot(algo_data['Optimal Cost'], p(algo_data['Optimal Cost']), 
                color=colors[idx], alpha=0.3, linestyle='--')
    
    plt.title('Steps vs Optimal Cost for 8-Puzzle', pad=20, fontsize=14)
    plt.xlabel('Optimal Solution Cost', fontsize=12)
    plt.ylabel('Steps Taken', fontsize=12)
    plt.legend(title='Algorithm', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Add grid for better readability
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / '8puzzle_steps_vs_optimal.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Value improvement distribution
    plt.figure(figsize=(12, 6))
    for problem in results['Problem'].unique():
        plt.subplot(1, 2, 1 if problem == '8-Puzzle' else 2)
        problem_data = results[results['Problem'] == problem]
        
        improvements = []
        labels = []
        for algo in problem_data['Algorithm'].unique():
            algo_data = problem_data[problem_data['Algorithm'] == algo]
            improvements.append(algo_data['Value Improvement'])
            labels.append(algo)
        
        plt.boxplot(improvements, labels=[l.replace(' (', '\n(') for l in labels])
        plt.title(f'{problem} Value Improvement', pad=20, fontsize=12)
        plt.ylabel('Improvement in Evaluation Value', fontsize=10)
        plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    plt.savefig(output_dir / 'value_improvements.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Create a summary table plot
    plt.figure(figsize=(12, 6))
    plt.axis('off')
    
    # Prepare summary data
    summary_data = []
    for problem in results['Problem'].unique():
        problem_data = results[results['Problem'] == problem]
        for algo in problem_data['Algorithm'].unique():
            algo_data = problem_data[problem_data['Algorithm'] == algo]
            success_rate = algo_data['Solution Found'].mean() * 100
            avg_steps = algo_data['Steps'].mean()
            avg_runtime = algo_data['Runtime'].mean()
            avg_improvement = algo_data['Value Improvement'].mean()
            summary_data.append([
                problem,
                algo,
                f'{success_rate:.1f}%',
                f'{avg_steps:.1f}',
                f'{avg_runtime:.3f}s',
                f'{avg_improvement:.2f}'
            ])
    
    # Create table
    table = plt.table(cellText=summary_data,
                     colLabels=['Problem', 'Algorithm', 'Success Rate', 'Avg Steps', 'Avg Runtime', 'Avg Improvement'],
                     loc='center',
                     cellLoc='center')
    
    # Adjust table style
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.5)
    
    # Add title
    plt.title('Summary of Results', pad=20, fontsize=14)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'summary_table.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    # Set up directories
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / 'data'
    figures_dir = base_dir / 'figures'
    
    # Run experiments
    print("Running 8-puzzle experiments...")
    puzzle_results = run_8puzzle_experiments()
    
    print("Running 8-queens experiments...")
    queens_results = run_8queens_experiments()
    
    # Combine results
    all_results = pd.concat([puzzle_results, queens_results], ignore_index=True)
    
    # Save raw results
    all_results.to_csv(data_dir / 'experiment_results.csv', index=False)
    
    # Create visualizations
    print("Generating plots...")
    plot_results(all_results, figures_dir)
    
    print("Experiments completed. Results saved to data/ and figures/ directories.")

if __name__ == "__main__":
    main() 