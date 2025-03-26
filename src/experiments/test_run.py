from .run_experiments import run_8puzzle_experiments, run_8queens_experiments
from ..utils.plot_results import plot_results
from pathlib import Path
import pandas as pd
import numpy as np

def generate_summary(df: pd.DataFrame, data_dir: Path) -> None:
    """Generate summary statistics from experiment results.
    
    Args:
        df (pd.DataFrame): DataFrame containing experiment results with columns:
            - Problem: Name of the problem
            - Algorithm: Name of the algorithm
            - Solution Found: Boolean indicating if solution was found
            - Steps: Number of steps taken
            - Runtime: Time taken in seconds
            - Value Improvement: Improvement in evaluation value
        data_dir (Path): Directory to save the summary CSV file
    
    The summary includes:
        - Solution Rate: Mean of Solution Found
        - Success %: Solution Rate in percentage format
        - Avg Steps: Mean number of steps
        - Steps Std: Standard deviation of steps
        - Avg Time: Mean runtime
        - Time Std: Standard deviation of runtime
        - Avg Improvement: Mean improvement in evaluation value
        - Improvement Std: Standard deviation of value improvement
    """
    # Calculate summary statistics
    summary = df.groupby(['Algorithm', 'Problem']).agg({
        'Solution Found': ['mean', lambda x: x.mean() * 100],  # Convert to percentage
        'Steps': ['mean', 'std'],
        'Runtime': ['mean', 'std'],
        'Value Improvement': ['mean', 'std']
    }).round(2)

    # Rename columns
    summary.columns = ['Solution Rate', 'Success %', 'Avg Steps', 'Steps Std', 'Avg Time', 'Time Std', 'Avg Improvement', 'Improvement Std']

    # Save summary to CSV
    summary.to_csv(data_dir / 'results_summary.csv')
    print("\nGenerated results summary in data/results_summary.csv")

def main():
    """Main function to run test experiments and generate visualizations.
    
    This function:
    1. Sets up necessary directories
    2. Runs 8-puzzle experiments with 50 instances
    3. Runs 8-queens experiments with 50 instances
    4. Combines results into a single DataFrame
    5. Generates summary statistics
    6. Creates visualizations
    7. Prints summary statistics to console
    
    The results are saved in:
        - data/puzzle_results.csv: Raw 8-puzzle results
        - data/queens_results.csv: Raw 8-queens results
        - data/experiment_results.csv: Combined results
        - data/results_summary.csv: Summary statistics
        - figures/: Directory containing all generated plots
    """
    try:
        # Set up directories
        data_dir = Path(__file__).parent.parent.parent / 'data'
        figures_dir = Path(__file__).parent.parent.parent / 'figures'
        data_dir.mkdir(parents=True, exist_ok=True)
        figures_dir.mkdir(parents=True, exist_ok=True)
        
        # Run 8-puzzle experiments
        print("\nRunning 8-puzzle experiments...")
        try:
            puzzle_results = run_8puzzle_experiments(num_instances=50)
            # Save intermediate results
            puzzle_results.to_csv(data_dir / 'puzzle_results.csv', index=False)
            print("\nSaved 8-puzzle results to data/puzzle_results.csv")
        except KeyboardInterrupt:
            print("\n8-puzzle experiments interrupted. Saving partial results...")
            if 'puzzle_results' in locals():
                puzzle_results.to_csv(data_dir / 'puzzle_results_partial.csv', index=False)
            return
        except Exception as e:
            print(f"\nError in 8-puzzle experiments: {str(e)}")
            print(f"Exception details: {e}")
            import traceback
            traceback.print_exc()
            return
        
        # Run 8-queens experiments
        print("\nRunning 8-queens experiments...")
        try:
            queens_results = run_8queens_experiments(num_instances=50)
            # Save intermediate results
            queens_results.to_csv(data_dir / 'queens_results.csv', index=False)
            print("\nSaved 8-queens results to data/queens_results.csv")
        except KeyboardInterrupt:
            print("\n8-queens experiments interrupted. Saving partial results...")
            if 'queens_results' in locals():
                queens_results.to_csv(data_dir / 'queens_results_partial.csv', index=False)
            return
        except Exception as e:
            print(f"\nError in 8-queens experiments: {str(e)}")
            print(f"Exception details: {e}")
            import traceback
            traceback.print_exc()
            return
        
        # Combine results
        print("\nCombining results...")
        all_results = pd.concat([puzzle_results, queens_results], ignore_index=True)
        
        # Save raw results
        all_results.to_csv(data_dir / 'experiment_results.csv', index=False)
        print("Saved combined results to data/experiment_results.csv")
        
        # Generate summary statistics
        print("\nGenerating summary statistics...")
        generate_summary(all_results, data_dir)
        print("Summary statistics saved to data/results_summary.csv")
        
        # Create visualizations
        print("\nGenerating plots...")
        try:
            plot_results(all_results, figures_dir)
            print("Plots saved to figures/ directory")
        except Exception as e:
            print(f"\nError generating plots: {str(e)}")
            import traceback
            traceback.print_exc()
            return
        
        # Print summary statistics
        print("\nSummary Statistics:")
        print("------------------")
        success_rates = all_results.groupby(['Problem', 'Algorithm'])['Solution Found'].mean() * 100
        print("\nSuccess Rates (%):")
        print(success_rates)
        
        avg_steps = all_results.groupby(['Problem', 'Algorithm'])['Steps'].mean()
        print("\nAverage Steps:")
        print(avg_steps)
        
        avg_runtime = all_results.groupby(['Problem', 'Algorithm'])['Runtime'].mean()
        print("\nAverage Runtime (seconds):")
        print(avg_runtime)
        
        print("\nExperiments completed. Results saved to data/ and figures/ directories.")
        
    except KeyboardInterrupt:
        print("\nTest script interrupted by user. Exiting...")
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        import traceback
        traceback.print_exc()
        raise

if __name__ == "__main__":
    main() 