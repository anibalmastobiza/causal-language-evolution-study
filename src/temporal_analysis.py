 import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy import stats
    from sklearn.linear_model import LinearRegression
    from typing import Dict, List, Tuple

    class TemporalAnalyzer:
        def __init__(self):
            self.decade_ranges = {
                '1950s': (1950, 1959),
                '1960s': (1960, 1969),
                '1970s': (1970, 1979),
                '1980s': (1980, 1989),
                '1990s': (1990, 1999),
                '2000s': (2000, 2009),
                '2010s': (2010, 2019),
                '2020s': (2020, 2025)
            }

        def assign_decades(self, df: pd.DataFrame, year_column: str = 
    'year') -> pd.DataFrame:
            """Assign decade labels to data."""
            df = df.copy()
            df['decade'] = df[year_column].apply(self._year_to_decade)
            return df

        def _year_to_decade(self, year: int) -> str:
            """Convert year to decade label."""
            for decade, (start, end) in self.decade_ranges.items():
                if start <= year <= end:
                    return decade
            return 'Unknown'

        def calculate_trend_statistics(self, df: pd.DataFrame, 
    metric_column: str, 
                                     year_column: str = 'year') -> 
    Dict[str, float]:
            """Calculate trend statistics for a given metric."""
            X = df[year_column].values.reshape(-1, 1)
            y = df[metric_column].values

            # Linear regression
            reg = LinearRegression().fit(X, y)
            slope = reg.coef_[0]
            r_squared = reg.score(X, y)

            # Pearson correlation
            corr_coef, p_value = stats.pearsonr(df[year_column],
    df[metric_column])

            return {
                'slope': slope,
                'r_squared': r_squared,
                'correlation': corr_coef,
                'p_value': p_value,
                'trend_significant': p_value < 0.05
            }

        def analyze_evolution_by_category(self, df: pd.DataFrame) -> 
    pd.DataFrame:
            """Analyze evolution of each causal category over time."""
            causal_categories = [
                'enablement_foundation_count',
                'inhibition_prevention_count',
                'reciprocal_causal_count',
                'phraseological_count',
                'statistical_terms_count',
                'mediation_moderation_count'
            ]

            results = []

            for category in causal_categories:
                if category in df.columns:
                    stats = self.calculate_trend_statistics(df, category)
                    stats['category'] = category.replace('_count', '')
                    results.append(stats)

            return pd.DataFrame(results)

        def create_evolution_plots(self, df: pd.DataFrame, output_dir: str 
    = '../results/'):
            """Create visualization plots for temporal evolution."""
            plt.style.use('seaborn-v0_8')

            # 1. Overall causal density evolution
            plt.figure(figsize=(12, 8))

            # Decade-wise analysis
            decade_stats = df.groupby('decade').agg({
                'causal_density': ['mean', 'std', 'count'],
                'total_causal_terms': ['mean', 'std']
            }).round(3)

            plt.subplot(2, 2, 1)
            sns.boxplot(data=df, x='decade', y='causal_density')
            plt.title('Causal Density Evolution by Decade')
            plt.xticks(rotation=45)

