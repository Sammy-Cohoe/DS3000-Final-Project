"""
DS3000 Final Project - Phase 1: Feature Engineering & Analysis
"""

from src.data.data_loader import load_data
from src.data.preprocessing import (check_missing_values, create_derived_features, encode_features)
from src.visualization.exploratory_analysis import (plot_feature_correlations, plot_top_features_scatter)


def main():
    print("=" * 60)
    print("DS3000 Final Project - Phase 1")
    print("Feature Engineering & Analysis")
    print("=" * 60)

    # Step 1: Preprocessing
    print("\n[STEP 1] Data Preprocessing")
    print("-" * 60)

    print("\n[1.1] Loading data...")
    data = load_data()
    print(f"✓ Loaded {data.shape[0]} samples with {data.shape[1]} features")

    print("\n[1.2] Checking for missing values...")
    check_missing_values(data)

    print("\n[1.3] Creating derived features...")
    data_enhanced = create_derived_features(data)

    print("\n[1.4] Encoding categorical features...")
    data_processed = encode_features(data_enhanced)

    print("\n[1.5] Saving processed data...")
    data_processed.to_csv('data/processed/CO2_processed.csv', index=False)
    print("✓ Saved to 'data/processed/CO2_processed.csv'")

    # Step 2: Feature Analysis
    print("\n" + "=" * 60)
    print("[STEP 2] Feature Analysis")
    print("-" * 60)

    print("\n[2.1] Analyzing feature correlations with CO2...")
    corr_df = plot_feature_correlations(data_processed)

    print("\nTop 10 Most Correlated Features:")
    print(corr_df.head(10))

    print("\n[2.2] Creating scatter plots for top features...")
    plot_top_features_scatter(data_processed)

    print("\n[2.3] Saving correlation results...")
    corr_df.to_csv('outputs/feature_correlations.csv')
    print("✓ Saved 'outputs/feature_correlations.csv'")

    # Summary
    print("\n" + "=" * 60)
    print("KEY FINDINGS:")
    print("=" * 60)

    strong_positive = corr_df[corr_df['Correlation'] > 0.7]
    strong_negative = corr_df[corr_df['Correlation'] < -0.7]

    if len(strong_positive) > 0:
        print(f"\nStrong POSITIVE correlations (increase CO2):")
        for feat, row in strong_positive.iterrows():
            print(f"  • {feat}: {row['Correlation']:.3f}")

    if len(strong_negative) > 0:
        print(f"\nStrong NEGATIVE correlations (decrease CO2):")
        for feat, row in strong_negative.iterrows():
            print(f"  • {feat}: {row['Correlation']:.3f}")

    print("\n" + "=" * 60)
    print("Phase 1 Complete!")
    print("Check outputs/figures/ for visualizations")
    print("=" * 60)


if __name__ == "__main__":
    main()
