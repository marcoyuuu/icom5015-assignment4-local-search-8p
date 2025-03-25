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
    """Create bar plot of success rates for a specific problem."""
    plt.figure(figsize=(10, 6))
    
    # Filter data for specific problem
    problem_data = df[df['Problem'] == problem]
    
    # Create bar plot
    bars = plt.bar(problem_data['Algorithm'], 
                   problem_data['Success %'],
                   color=[ALGORITHM_COLORS[alg] for alg in problem_data['Algorithm']])
    
    # Customize plot
    plt.title(f'Success Rate on {problem}', fontsize=14, pad=20)
    plt.ylabel('Success Rate (%)', fontsize=12)
    plt.xlabel('Algorithm', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%',
                ha='center', va='bottom')
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    os.makedirs('figures', exist_ok=True)
    plt.savefig(f'figures/{problem.lower().replace("-", "_")}_success.png',
                dpi=300, bbox_inches='tight')
    plt.close()

def create_steps_plot(df, problem):
    """Create bar plot of average steps for a specific problem."""
    plt.figure(figsize=(10, 6))
    
    # Filter data for specific problem
    problem_data = df[df['Problem'] == problem]
    
    # Create bar plot
    bars = plt.bar(problem_data['Algorithm'], 
                   problem_data['Avg Steps'],
                   color=[ALGORITHM_COLORS[alg] for alg in problem_data['Algorithm']])
    
    # Customize plot
    plt.title(f'Average Steps on {problem}', fontsize=14, pad=20)
    plt.ylabel('Average Number of Steps', fontsize=12)
    plt.xlabel('Algorithm', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}',
                ha='center', va='bottom')
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    os.makedirs('figures', exist_ok=True)
    plt.savefig(f'figures/{problem.lower().replace("-", "_")}_steps.png',
                dpi=300, bbox_inches='tight')
    plt.close()

def create_runtime_plot(df, problem):
    """Create bar plot of average runtime for a specific problem."""
    plt.figure(figsize=(10, 6))
    
    # Filter data for specific problem
    problem_data = df[df['Problem'] == problem]
    
    # Create bar plot
    bars = plt.bar(problem_data['Algorithm'], 
                   problem_data['Avg Time'],
                   color=[ALGORITHM_COLORS[alg] for alg in problem_data['Algorithm']])
    
    # Customize plot
    plt.title(f'Average Runtime on {problem}', fontsize=14, pad=20)
    plt.ylabel('Average Runtime (seconds)', fontsize=12)
    plt.xlabel('Algorithm', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.6f}',
                ha='center', va='bottom')
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    os.makedirs('figures', exist_ok=True)
    plt.savefig(f'figures/{problem.lower().replace("-", "_")}_runtime.png',
                dpi=300, bbox_inches='tight')
    plt.close()

def create_comparison_plot(df):
    """Create side-by-side comparison of success rates for both problems."""
    plt.figure(figsize=(12, 6))
    
    # Prepare data for grouped bar plot
    algorithms = df['Algorithm'].unique()
    problems = df['Problem'].unique()
    
    x = np.arange(len(algorithms))
    width = 0.35
    
    # Create bars for each problem
    for i, problem in enumerate(problems):
        problem_data = df[df['Problem'] == problem]
        plt.bar(x + i*width, problem_data['Success %'], width,
                label=problem, color=[ALGORITHM_COLORS[alg] for alg in algorithms])
    
    # Customize plot
    plt.title('Success Rate Comparison Across Problems', fontsize=14, pad=20)
    plt.ylabel('Success Rate (%)', fontsize=12)
    plt.xlabel('Algorithm', fontsize=12)
    plt.xticks(x + width/2, algorithms, rotation=45, ha='right')
    plt.legend()
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    os.makedirs('figures', exist_ok=True)
    plt.savefig('figures/success_rate_comparison.png',
                dpi=300, bbox_inches='tight')
    plt.close()

def create_performance_matrix(df):
    """Create a heatmap of performance metrics across algorithms and problems."""
    plt.figure(figsize=(12, 8))
    
    # Prepare data for heatmap
    metrics = ['Success %', 'Avg Steps', 'Avg Time']
    pivot_data = df.pivot(index='Problem', columns='Algorithm', values=metrics)
    
    # Create heatmap
    sns.heatmap(pivot_data, annot=True, fmt='.2f', cmap='YlOrRd')
    
    # Customize plot
    plt.title('Performance Matrix Across Problems and Algorithms', fontsize=14, pad=20)
    plt.xlabel('Algorithm', fontsize=12)
    plt.ylabel('Problem', fontsize=12)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    os.makedirs('figures', exist_ok=True)
    plt.savefig('figures/performance_matrix.png',
                dpi=300, bbox_inches='tight')
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