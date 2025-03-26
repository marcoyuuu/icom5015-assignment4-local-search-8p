import sys
from pathlib import Path
import os
import pandas as pd
from src.utils.plot_results import (
    create_success_rate_plot,
    create_steps_plot,
    create_runtime_plot,
    create_comparison_plot,
    create_performance_matrix
)

def setup_environment():
    """Set up the Python environment and create necessary directories."""
    # Add src directory to Python path
    src_path = Path(__file__).parent / 'src'
    if str(src_path) not in sys.path:
        sys.path.append(str(src_path))
    
    # Create directories if they don't exist
    data_dir = Path(__file__).parent / 'data'
    figures_dir = Path(__file__).parent / 'figures'
    data_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)
    
    return data_dir, figures_dir

def generate_puzzle_results():
    """Generate results for 8-puzzle experiments directly."""
    data_dir, figures_dir = setup_environment()
    
    # Import necessary functions
    from src.local_search.algorithms import (
        hill_climbing_steepest,
        hill_climbing_first_choice,
        hill_climbing_random_restart,
        simulated_annealing,
        exponential_schedule,
        linear_schedule
    )
    from src.puzzle8.generator import (
        generate_8puzzle_instance,
        get_manhattan_distance,
        get_valid_moves,
        apply_move
    )
    import pandas as pd
    import time
    
    results = []
    num_instances = 50
    print(f"\nRunning 8-puzzle experiments with {num_instances} instances...")
    
    for i in range(num_instances):
        try:
            # Generate a random puzzle
            initial_state = generate_8puzzle_instance()
            
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
                    generate_8puzzle_instance,
                    max_restarts=10
                ),
                'Simulated Annealing (Exponential)': lambda: simulated_annealing(
                    initial_state,
                    lambda s: [apply_move(s, m) for m in get_valid_moves(s.index(0))],
                    evaluate,
                    exponential_schedule(k=30, lam=0.001)
                ),
                'Simulated Annealing (Linear)': lambda: simulated_annealing(
                    initial_state,
                    lambda s: [apply_move(s, m) for m in get_valid_moves(s.index(0))],
                    evaluate,
                    linear_schedule
                )
            }
            
            print(f"Instance {i+1}/{num_instances} - Testing all algorithms...")
            
            for algo_name, algo_func in algorithms.items():
                print(f"  Running {algo_name}...", end='')
                try:
                    start_time = time.time()
                    final_state, value_history = algo_func()
                    runtime = time.time() - start_time
                    
                    # Calculate additional metrics
                    initial_value = evaluate(initial_state)
                    final_value = evaluate(final_state)
                    improvement = initial_value - final_value
                    solution_found = get_manhattan_distance(final_state) == 0
                    steps = len(value_history) - 1
                    
                    results.append({
                        'Problem': '8-Puzzle',
                        'Instance': i,
                        'Algorithm': algo_name,
                        'Initial State': initial_state,
                        'Final State': final_state,
                        'Initial Value': initial_value,
                        'Final Value': final_value,
                        'Value Improvement': improvement,
                        'Solution Found': solution_found,
                        'Steps': steps,
                        'Runtime': runtime,
                        'Value History': value_history
                    })
                    print(f" done. {'Solution found!' if solution_found else 'No solution.'} Steps: {steps}")
                except Exception as e:
                    print(f" error: {str(e)}")
                    continue
            
        except Exception as e:
            print(f"Error processing instance {i}: {str(e)}")
            continue
    
    # Save results
    results_df = pd.DataFrame(results)
    results_df.to_csv(data_dir / 'puzzle_results.csv', index=False)
    print(f"Saved {len(results)} results to data/puzzle_results.csv")
    
    return results_df

def generate_queens_results():
    """Generate results for 8-queens experiments."""
    data_dir, figures_dir = setup_environment()
    
    # Import necessary functions
    from src.local_search.algorithms import (
        hill_climbing_steepest,
        hill_climbing_first_choice,
        hill_climbing_random_restart,
        simulated_annealing,
        exponential_schedule,
        linear_schedule
    )
    from src.queens8.generator import (
        generate_8queens_state,
        count_conflicts,
        get_neighbors
    )
    import pandas as pd
    import time
    
    results = []
    num_instances = 50
    print(f"\nRunning 8-queens experiments with {num_instances} instances...")
    
    for i in range(num_instances):
        try:
            # Generate a random queens configuration
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
                    generate_8queens_state,
                    max_restarts=10
                ),
                'Simulated Annealing (Exponential)': lambda: simulated_annealing(
                    initial_state,
                    get_neighbors,
                    evaluate,
                    exponential_schedule(k=30, lam=0.001)
                ),
                'Simulated Annealing (Linear)': lambda: simulated_annealing(
                    initial_state,
                    get_neighbors,
                    evaluate,
                    linear_schedule
                )
            }
            
            print(f"Instance {i+1}/{num_instances} - Testing all algorithms...")
            
            for algo_name, algo_func in algorithms.items():
                print(f"  Running {algo_name}...", end='')
                try:
                    start_time = time.time()
                    final_state, value_history = algo_func()
                    runtime = time.time() - start_time
                    
                    # Calculate additional metrics
                    initial_value = evaluate(initial_state)
                    final_value = evaluate(final_state)
                    improvement = initial_value - final_value
                    solution_found = count_conflicts(final_state) == 0
                    steps = len(value_history) - 1
                    
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
                        'Steps': steps,
                        'Runtime': runtime,
                        'Value History': value_history
                    })
                    print(f" done. {'Solution found!' if solution_found else 'No solution.'} Steps: {steps}")
                except Exception as e:
                    print(f" error: {str(e)}")
                    continue
            
        except Exception as e:
            print(f"Error processing instance {i}: {str(e)}")
            continue
    
    # Save results
    results_df = pd.DataFrame(results)
    results_df.to_csv(data_dir / 'queens_results.csv', index=False)
    print(f"Saved {len(results)} results to data/queens_results.csv")
    
    return results_df

def calculate_summary_statistics(df):
    """Calculate summary statistics for plotting.
    
    Args:
        df (pd.DataFrame): DataFrame containing experiment results with columns:
            - Problem: Name of the problem ('8-Puzzle' or '8-Queens')
            - Algorithm: Name of the algorithm used
            - Solution Found: Boolean indicating if solution was found
            - Steps: Number of steps taken
            - Runtime: Time taken in seconds
    
    Returns:
        pd.DataFrame: DataFrame with summary statistics including:
            - Solution Rate: Mean of Solution Found
            - Solution Std: Standard deviation of Solution Found
            - Avg Steps: Mean number of steps
            - Steps Std: Standard deviation of steps
            - Avg Time: Mean runtime
            - Time Std: Standard deviation of runtime
            - Success %: Solution Rate in percentage format
    """
    # Group by Problem and Algorithm and calculate statistics
    summary_stats = df.groupby(['Problem', 'Algorithm']).agg({
        'Solution Found': ['mean', 'std'],
        'Steps': ['mean', 'std'],
        'Runtime': ['mean', 'std']
    })

    # Rename columns for clarity
    summary_stats.columns = [
        'Solution Rate', 'Solution Std',
        'Avg Steps', 'Steps Std',
        'Avg Time', 'Time Std'
    ]

    # Add Success % column (same as Solution Rate but in percentage format)
    summary_stats['Success %'] = summary_stats['Solution Rate'] * 100

    # Reset index to convert MultiIndex to regular columns
    summary_stats = summary_stats.reset_index()

    return summary_stats

def generate_summary(df: pd.DataFrame, data_dir: str) -> None:
    """Generate summary statistics and save to CSV.
    
    Args:
        df (pd.DataFrame): DataFrame containing experiment results
        data_dir (str): Directory to save the summary CSV file
    
    The summary includes:
        - Solution Rate: Mean of Solution Found
        - Solution Std: Standard deviation of Solution Found
        - Num Instances: Count of instances
        - Avg Steps: Mean number of steps
        - Steps Std: Standard deviation of steps
        - Avg Runtime: Mean runtime
        - Runtime Std: Standard deviation of runtime
        - Avg Value Improvement: Mean improvement in evaluation value
        - Value Improvement Std: Standard deviation of value improvement
    """
    # Calculate summary statistics
    summary = df.groupby(['Problem', 'Algorithm']).agg({
        'Solution Found': ['mean', 'std', 'count'],
        'Steps': ['mean', 'std'],
        'Runtime': ['mean', 'std'],
        'Value Improvement': ['mean', 'std']
    }).round(2)

    # Rename columns for clarity
    summary.columns = [
        'Solution Rate', 'Solution Std', 'Num Instances',
        'Avg Steps', 'Steps Std',
        'Avg Runtime', 'Runtime Std',
        'Avg Value Improvement', 'Value Improvement Std'
    ]

    # Save to CSV
    summary.to_csv(os.path.join(data_dir, 'results_summary.csv'))

def main():
    """Main function to run all experiments and generate visualizations.
    
    This function:
    1. Creates necessary directories (data/ and figures/)
    2. Runs 8-puzzle experiments and saves results
    3. Runs 8-queens experiments and saves results
    4. Combines results into a single DataFrame
    5. Generates summary statistics
    6. Creates visualizations including:
       - Success rate plots for each problem
       - Steps plots for each problem
       - Runtime plots for each problem
       - Comparison plots across problems
       - Performance matrix
    """
    # Create directories if they don't exist
    os.makedirs('data', exist_ok=True)
    os.makedirs('figures', exist_ok=True)

    # Run experiments
    print("Running 8-puzzle experiments...")
    puzzle_results = generate_puzzle_results()
    puzzle_results.to_csv('data/puzzle_results.csv', index=False)
    print(f"Saved {len(puzzle_results)} results to data/puzzle_results.csv")

    print("\nRunning 8-queens experiments...")
    queens_results = generate_queens_results()
    queens_results.to_csv('data/queens_results.csv', index=False)
    print(f"Saved {len(queens_results)} results to data/queens_results.csv")

    print("\nCombining results...")
    # Combine results
    all_results = pd.concat([puzzle_results, queens_results])
    all_results.to_csv('data/experiment_results.csv', index=False)
    print("Combined results saved to data/experiment_results.csv")

    print("\nGenerating summary statistics...")
    # Generate summary statistics
    generate_summary(all_results, 'data')
    print("Summary statistics saved to data/results_summary.csv")

    print("\nCalculating summary statistics for plotting...")
    summary_results = calculate_summary_statistics(all_results)

    print("\nGenerating plots...")
    # Generate plots for each problem
    for problem in ['8-Puzzle', '8-Queens']:
        problem_data = summary_results[summary_results['Problem'] == problem]
        create_success_rate_plot(summary_results, problem)
        create_steps_plot(summary_results, problem)
        create_runtime_plot(summary_results, problem)

    # Create comparison plots
    create_comparison_plot(summary_results)
    create_performance_matrix(summary_results)

if __name__ == '__main__':
    main() 