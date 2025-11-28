import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import pearsonr


def plot_distributions(data):
    """Create histograms for all numeric features"""
    data.hist(figsize=(12, 8), bins=20)
    plt.tight_layout()
    plt.savefig('outputs/figures/distributions.png')
    plt.show()
    print("Distribution plots saved as 'outputs/figures/distributions.png'")


def correlation_heatmap(data):
    """Create correlation heatmap for numeric features"""
    numeric_data = data.select_dtypes(include=['float64', 'int64'])

    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('outputs/figures/correlation_heatmap.png')
    plt.show()
    print("Correlation heatmap saved as 'outputs/figures/correlation_heatmap.png'")


def plot_feature_correlations(data, target_column='CO2 Emissions(g/km)'):
    """Plot feature correlations with target variable"""
    X = data.drop(columns=[target_column])
    y = data[target_column]

    correlations = {}
    for col in X.columns:
        if data[col].dtype in ['float64', 'int64']:
            corr, _ = pearsonr(data[col], y)
            correlations[col] = corr

    # Sort by absolute correlation
    corr_df = pd.DataFrame.from_dict(correlations, orient='index', columns=['Correlation'])
    corr_df['Abs_Correlation'] = corr_df['Correlation'].abs()
    corr_df = corr_df.sort_values('Abs_Correlation', ascending=False)

    # Bar plot
    plt.figure(figsize=(10, 6))
    top_features = corr_df.head(10)
    colors = ['red' if x < 0 else 'green' for x in top_features['Correlation']]
    plt.barh(range(len(top_features)), top_features['Correlation'], color=colors)
    plt.yticks(range(len(top_features)), top_features.index)
    plt.xlabel('Correlation with CO2 Emissions')
    plt.title('Top 10 Features Correlated with CO2 Emissions')
    plt.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
    plt.tight_layout()
    plt.savefig('outputs/figures/feature_correlations.png')
    print("✓ Saved 'outputs/figures/feature_correlations.png'")

    return corr_df


def plot_top_features_scatter(data, target_column='CO2 Emissions(g/km)', top_n=6):
    """Create scatter plots for top correlated features"""
    X = data.drop(columns=[target_column])
    y = data[target_column]

    # Get correlations
    correlations = {}
    for col in X.columns:
        if data[col].dtype in ['float64', 'int64']:
            corr, _ = pearsonr(data[col], y)
            correlations[col] = corr

    # Get top features
    corr_df = pd.DataFrame.from_dict(correlations, orient='index', columns=['Correlation'])
    corr_df['Abs_Correlation'] = corr_df['Correlation'].abs()
    top_features = corr_df.sort_values('Abs_Correlation', ascending=False).head(top_n).index.tolist()

    # Create scatter plots
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()

    for idx, feature in enumerate(top_features):
        axes[idx].scatter(data[feature], y, alpha=0.5, s=10)
        axes[idx].set_xlabel(feature)
        axes[idx].set_ylabel('CO2 Emissions (g/km)')
        axes[idx].set_title(f'{feature} vs CO2\nCorr: {correlations[feature]:.3f}')

    plt.tight_layout()
    plt.savefig('outputs/figures/top_features_scatter.png')
    print("✓ Saved 'outputs/figures/top_features_scatter.png'")


def exploratory_plots(data):
    """Generate exploratory visualizations"""
    plot_distributions(data)
    correlation_heatmap(data)
