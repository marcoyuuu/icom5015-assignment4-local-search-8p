import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import numpy as np
from matplotlib.gridspec import GridSpec

# Set seaborn style
sns.set_theme(style="whitegrid")

# Consistent colors for algorithms
ALGORITHM_COLORS = {
    'Hill Climbing (Steepest)': '#FF9999',
    'Hill Climbing (First Choice)': '#66B2FF',
    'Hill Climbing (Random Restart)': '#99FF99',
    'Simulated Annealing (Exponential)': '#FFCC99',
    'Simulated Annealing (Linear)': '#FF99CC'
}

def set_ieee_style():
    """Set IEEE-compatible plotting style"""
    plt.style.use('default')
    plt.rcParams.update({
        'font.size': 10,
        'font.family': 'serif',
        'font.serif': ['Times New Roman'],
        'figure.dpi': 300,
        'figure.figsize': (8, 6),
        'axes.grid': True,
        'grid.linestyle': '--',
        'grid.alpha': 0.7,
    })

def create_success_rate_plot(df, problem):
    """Create a bar plot of success rates for a specific problem.
    
    Args:
        df (pd.DataFrame): DataFrame containing summary statistics with columns:
            - Problem: Name of the problem
            - Algorithm: Name of the algorithm
            - Success %: Success rate in percentage
        problem (str): Name of the problem to plot ('8-Puzzle' or '8-Queens')
    
    The plot shows:
        - Success rate for each algorithm on the specified problem
        - Error bars showing standard deviation
        - Clear labels and legend
    """
    # Filter data for the specific problem
    problem_data = df[df['Problem'] == problem]
    
    # Create bar plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(problem_data['Algorithm'], problem_data['Success %'],
                   yerr=problem_data['Solution Std'] * 100,
                   capsize=5)
    
    # Customize plot
    plt.title(f'Success Rate by Algorithm - {problem}', pad=20)
    plt.xlabel('Algorithm')
    plt.ylabel('Success Rate (%)')
    plt.xticks(rotation=45, ha='right')
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%',
                ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig(f'figures/{problem.lower().replace("-", "_")}_success.png')
    plt.close()

def create_steps_plot(df, problem):
    """Create a bar plot of average steps for a specific problem.
    
    Args:
        df (pd.DataFrame): DataFrame containing summary statistics with columns:
            - Problem: Name of the problem
            - Algorithm: Name of the algorithm
            - Avg Steps: Mean number of steps
            - Steps Std: Standard deviation of steps
        problem (str): Name of the problem to plot ('8-Puzzle' or '8-Queens')
    
    The plot shows:
        - Average steps for each algorithm on the specified problem
        - Error bars showing standard deviation
        - Clear labels and legend
    """
    # Filter data for the specific problem
    problem_data = df[df['Problem'] == problem]
    
    # Create bar plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(problem_data['Algorithm'], problem_data['Avg Steps'],
                   yerr=problem_data['Steps Std'],
                   capsize=5)
    
    # Customize plot
    plt.title(f'Average Steps by Algorithm - {problem}', pad=20)
    plt.xlabel('Algorithm')
    plt.ylabel('Number of Steps')
    plt.xticks(rotation=45, ha='right')
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}',
                ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig(f'figures/{problem.lower().replace("-", "_")}_steps.png')
    plt.close()

def create_runtime_plot(df, problem):
    """Create a bar plot of average runtime for a specific problem.
    
    Args:
        df (pd.DataFrame): DataFrame containing summary statistics with columns:
            - Problem: Name of the problem
            - Algorithm: Name of the algorithm
            - Avg Time: Mean runtime
            - Time Std: Standard deviation of runtime
        problem (str): Name of the problem to plot ('8-Puzzle' or '8-Queens')
    
    The plot shows:
        - Average runtime for each algorithm on the specified problem
        - Error bars showing standard deviation
        - Clear labels and legend
    """
    # Filter data for the specific problem
    problem_data = df[df['Problem'] == problem]
    
    # Create bar plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(problem_data['Algorithm'], problem_data['Avg Time'],
                   yerr=problem_data['Time Std'],
                   capsize=5)
    
    # Customize plot
    plt.title(f'Average Runtime by Algorithm - {problem}', pad=20)
    plt.xlabel('Algorithm')
    plt.ylabel('Runtime (seconds)')
    plt.xticks(rotation=45, ha='right')
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}s',
                ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig(f'figures/{problem.lower().replace("-", "_")}_runtime.png')
    plt.close()

def create_comparison_plot(df):
    """Create a comparison plot showing success rates across problems.
    
    Args:
        df (pd.DataFrame): DataFrame containing summary statistics with columns:
            - Problem: Name of the problem
            - Algorithm: Name of the algorithm
            - Success %: Success rate in percentage
    
    The plot shows:
        - Success rates for each algorithm on both problems
        - Side-by-side comparison for easy visualization
        - Clear labels and legend
    """
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Plot for each problem
    for idx, problem in enumerate(['8-Puzzle', '8-Queens']):
        problem_data = df[df['Problem'] == problem]
        ax = ax1 if idx == 0 else ax2
        
        bars = ax.bar(problem_data['Algorithm'], problem_data['Success %'])
        ax.set_title(f'Success Rate - {problem}')
        ax.set_xlabel('Algorithm')
        ax.set_ylabel('Success Rate (%)')
        ax.tick_params(axis='x', rotation=45, ha='right')
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}%',
                   ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('figures/success_rate_comparison.png')
    plt.close()

def create_performance_matrix(df):
    """Create a performance matrix showing all metrics for all algorithms.
    
    Args:
        df (pd.DataFrame): DataFrame containing summary statistics with columns:
            - Problem: Name of the problem
            - Algorithm: Name of the algorithm
            - Success %: Success rate in percentage
            - Avg Steps: Mean number of steps
            - Avg Time: Mean runtime
    
    The plot shows:
        - A matrix of subplots for each metric
        - Comparison across problems and algorithms
        - Clear labels and color coding
    """
    # Create figure with subplots for each metric
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    axes = axes.ravel()
    
    # Metrics to plot
    metrics = [
        ('Success %', 'Success Rate (%)'),
        ('Avg Steps', 'Number of Steps'),
        ('Avg Time', 'Runtime (seconds)')
    ]
    
    # Plot each metric
    for idx, (metric, label) in enumerate(metrics):
        ax = axes[idx]
        
        # Plot for each problem
        for problem in ['8-Puzzle', '8-Queens']:
            problem_data = df[df['Problem'] == problem]
            x = np.arange(len(problem_data['Algorithm']))
            width = 0.35
            
            bars = ax.bar(x + width/2 if problem == '8-Queens' else x - width/2,
                         problem_data[metric],
                         width,
                         label=problem)
            
            # Add value labels
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.1f}{"%" if metric == "Success %" else ""}',
                       ha='center', va='bottom')
        
        ax.set_title(f'{label} by Algorithm')
        ax.set_xlabel('Algorithm')
        ax.set_ylabel(label)
        ax.set_xticks(x)
        ax.set_xticklabels(problem_data['Algorithm'], rotation=45, ha='right')
        ax.legend()
    
    # Remove the last subplot if we have an odd number of metrics
    if len(metrics) < 4:
        axes[-1].remove()
    
    plt.tight_layout()
    plt.savefig('figures/performance_matrix.png')
    plt.close()

def create_combined_metrics_plot(df, problem):
    """Create a combined plot showing success rate, steps, and runtime"""
    set_ieee_style()
    fig = plt.figure(figsize=(15, 5))
    gs = GridSpec(1, 3, figure=fig)
    
    # Success Rate
    ax1 = fig.add_subplot(gs[0])
    problem_data = df[df['Problem'] == problem]
    sns.barplot(data=problem_data, x='Algorithm', y='Success %', ax=ax1)
    ax1.set_title('Success Rate')
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')
    
    # Average Steps
    ax2 = fig.add_subplot(gs[1])
    sns.barplot(data=problem_data, x='Algorithm', y='Avg Steps', ax=ax2)
    ax2.set_title('Average Steps')
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
    
    # Runtime
    ax3 = fig.add_subplot(gs[2])
    sns.barplot(data=problem_data, x='Algorithm', y='Avg Time', ax=ax3)
    ax3.set_title('Average Runtime (s)')
    ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    return fig

def create_algorithm_comparison_heatmap(df):
    """Create a heatmap comparing algorithm performance across problems"""
    set_ieee_style()
    
    # Pivot the data for the heatmap
    metrics = ['Success %', 'Avg Steps', 'Avg Time']
    pivot_data = {}
    
    for metric in metrics:
        pivot_data[metric] = df.pivot(
            index='Problem', 
            columns='Algorithm',
            values=metric
        )
    
    # Create heatmap
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    for ax, (metric, data) in zip(axes, pivot_data.items()):
        sns.heatmap(data, annot=True, fmt='.2f', cmap='YlOrRd', ax=ax)
        ax.set_title(metric)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    return fig

def create_performance_profile(df, problem):
    """Create a radar chart showing algorithm performance profile"""
    set_ieee_style()
    
    problem_data = df[df['Problem'] == problem]
    metrics = ['Success %', 'Avg Steps', 'Avg Time']
    
    # Normalize the metrics
    normalized_data = {}
    for metric in metrics:
        if metric == 'Success %':
            normalized_data[metric] = problem_data[metric] / 100
        else:
            normalized_data[metric] = (problem_data[metric] - problem_data[metric].min()) / \
                                    (problem_data[metric].max() - problem_data[metric].min())
    
    # Create radar chart
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
    
    angles = np.linspace(0, 2*np.pi, len(metrics), endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))  # complete the circle
    
    for algorithm in problem_data['Algorithm']:
        values = [normalized_data[metric][problem_data['Algorithm'] == algorithm].iloc[0] 
                 for metric in metrics]
        values = np.concatenate((values, [values[0]]))  # complete the circle
        ax.plot(angles, values, label=algorithm)
        ax.fill(angles, values, alpha=0.1)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(metrics)
    ax.set_title(f'Algorithm Performance Profile - {problem}')
    plt.legend(bbox_to_anchor=(1.2, 0.5))
    
    return fig

def create_convergence_plot(steps_data, problem):
    """Create a plot showing convergence behavior"""
    set_ieee_style()
    
    fig, ax = plt.subplots()
    
    for algorithm in steps_data:
        ax.plot(steps_data[algorithm], label=algorithm)
    
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Solution Quality')
    ax.set_title(f'Convergence Behavior - {problem}')
    ax.legend()
    
    return fig

def export_all_visualizations(df, output_dir='figures/'):
    """Export all visualizations to the specified directory"""
    os.makedirs(output_dir, exist_ok=True)
    
    # Combined metrics plots
    for problem in ['8-Puzzle', '8-Queens']:
        fig = create_combined_metrics_plot(df, problem)
        fig.savefig(f'{output_dir}{problem.lower()}_combined_metrics.png', 
                   bbox_inches='tight', dpi=300)
        plt.close(fig)
        
        fig = create_performance_profile(df, problem)
        fig.savefig(f'{output_dir}{problem.lower()}_performance_profile.png',
                   bbox_inches='tight', dpi=300)
        plt.close(fig)
    
    # Algorithm comparison heatmap
    fig = create_algorithm_comparison_heatmap(df)
    fig.savefig(f'{output_dir}algorithm_comparison_heatmap.png',
                bbox_inches='tight', dpi=300)
    plt.close(fig)

def main():
    # Read data
    df = pd.read_csv('data/results_summary.csv')
    
    # Create plots for each problem
    for problem in ['8-Puzzle', '8-Queens']:
        create_success_rate_plot(df, problem)
        create_steps_plot(df, problem)
        create_runtime_plot(df, problem)
    
    # Create comparison plots
    create_comparison_plot(df)
    create_performance_matrix(df)
    
    # Export all visualizations
    export_all_visualizations(df)

if __name__ == '__main__':
    main() 