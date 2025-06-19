import pandas as pd
    import numpy as np
    from scipy import stats
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LinearRegression, LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import r2_score, classification_report
    import matplotlib.pyplot as plt
    import seaborn as sns
    from typing import Dict, List, Tuple, Optional
    import warnings
    warnings.filterwarnings('ignore')

    class StatisticalAnalyzer:
        def __init__(self):
            self.results = {}
            self.visualizations = []

        def descriptive_statistics(self, df: pd.DataFrame) -> Dict:
            """Generate comprehensive descriptive statistics."""
            desc_stats = {}

            # Overall corpus statistics
            desc_stats['corpus_overview'] = {
                'total_abstracts': len(df),
                'year_range': (df['year'].min(), df['year'].max()),
                'mean_causal_density': df['causal_density'].mean(),
                'std_causal_density': df['causal_density'].std(),
                'median_causal_density': df['causal_density'].median()
            }

            # Temporal statistics
            temporal_stats = df.groupby('decade').agg({
                'causal_density': ['count', 'mean', 'std', 'median'],
                'total_causal_terms': ['mean', 'std'],
                'enablement_foundation_count': 'mean',
                'inhibition_prevention_count': 'mean',
                'statistical_terms_count': 'mean'
            }).round(3)

            desc_stats['temporal_statistics'] = temporal_stats.to_dict()

            # Subdiscipline statistics
            if 'subdiscipline' in df.columns:
                subdiscipline_stats = df.groupby('subdiscipline').agg({
                    'causal_density': ['count', 'mean', 'std'],
                    'total_causal_terms': ['mean', 'std']
                }).round(3)
                desc_stats['subdiscipline_statistics'] =
    subdiscipline_stats.to_dict()

            return desc_stats

        def temporal_trend_analysis(self, df: pd.DataFrame) -> Dict:
            """Analyze temporal trends in causal language usage."""
            trend_results = {}

            # Overall causal density trend
            X = df['year'].values.reshape(-1, 1)
            y = df['causal_density'].values

            reg = LinearRegression().fit(X, y)
            trend_results['overall_trend'] = {
                'slope': reg.coef_[0],
                'intercept': reg.intercept_,
                'r_squared': reg.score(X, y),
                'correlation': stats.pearsonr(df['year'],
    df['causal_density'])[0],
                'p_value': stats.pearsonr(df['year'],
    df['causal_density'])[1]
            }

            # Category-specific trends
            causal_categories = [col for col in df.columns if
    col.endswith('_count')]

            category_trends = {}
            for category in causal_categories:
                if category in df.columns:
                    corr, p_val = stats.pearsonr(df['year'], df[category])

                    # Linear regression for slope
                    X_cat = df['year'].values.reshape(-1, 1)
                    y_cat = df[category].values
                    reg_cat = LinearRegression().fit(X_cat, y_cat)

                    category_trends[category] = {
                        'correlation': corr,
                        'p_value': p_val,
                        'slope': reg_cat.coef_[0],
                        'significant': p_val < 0.05,
                        'trend_direction': 'increasing' if reg_cat.coef_[0]
     > 0 else 'decreasing'
                    }

            trend_results['category_trends'] = category_trends

            return trend_results

        def subdiscipline_comparison(self, df: pd.DataFrame) -> Dict:
            """Compare causal language usage across philosophical 
    subdisciplines."""
            if 'subdiscipline' not in df.columns:
                return {'error': 'Subdiscipline column not found'}

            comparison_results = {}

            # ANOVA for causal density across subdisciplines
            subdisciplines = df['subdiscipline'].unique()
            causal_density_groups = [df[df['subdiscipline'] ==
    sub]['causal_density'].values
                                    for sub in subdisciplines]

            f_stat, p_value = stats.f_oneway(*causal_density_groups)
            comparison_results['anova_causal_density'] = {
                'f_statistic': f_stat,
                'p_value': p_value,
                'significant': p_value < 0.05
            }

            # Post-hoc pairwise comparisons (Tukey HSD simulation)
            pairwise_results = {}
            for i, sub1 in enumerate(subdisciplines):
                for j, sub2 in enumerate(subdisciplines[i+1:], i+1):
                    group1 = df[df['subdiscipline'] ==
    sub1]['causal_density']
                    group2 = df[df['subdiscipline'] ==
    sub2]['causal_density']

                    t_stat, p_val = stats.ttest_ind(group1, group2)
                    pairwise_results[f'{sub1}_vs_{sub2}'] = {
                        't_statistic': t_stat,
                        'p_value': p_val,
                        'significant': p_val < 0.05,
                        'effect_size': (group1.mean() - group2.mean()) /
    np.sqrt((group1.var() + group2.var()) / 2)
                    }

            comparison_results['pairwise_comparisons'] = pairwise_results

            return comparison_results

        def survey_analysis(self, survey_df: pd.DataFrame) -> Dict:
            """Analyze survey responses on causal language clarity."""
            survey_results = {}

            # Clarity ratings analysis
            clarity_columns = [col for col in survey_df.columns if
    'clarity_rating' in col]
            if clarity_columns:
                clarity_stats = survey_df[clarity_columns].describe()
                survey_results['clarity_statistics'] =
    clarity_stats.to_dict()

                # Compare high vs low density abstract ratings
                high_density_ratings = [col for col in clarity_columns if
    '_a' in col]  # Abstract A = high density
                low_density_ratings = [col for col in clarity_columns if
    '_b' in col]   # Abstract B = low density

                if high_density_ratings and low_density_ratings:
                    high_mean =
    survey_df[high_density_ratings].mean().mean()
                    low_mean = survey_df[low_density_ratings].mean().mean()

                    # Paired t-test
                    paired_diff = []
                    for hd_col, ld_col in zip(high_density_ratings,
    low_density_ratings):
                        if hd_col in survey_df.columns and ld_col in
    survey_df.columns:
                            diff = survey_df[hd_col] - survey_df[ld_col]
                            paired_diff.extend(diff.dropna().tolist())

                    if paired_diff:
                        t_stat, p_val = stats.ttest_1samp(paired_diff, 0)
                        survey_results['clarity_comparison'] = {
                            'high_density_mean': high_mean,
                            'low_density_mean': low_mean,
                            'mean_difference': np.mean(paired_diff),
                            't_statistic': t_stat,
                            'p_value': p_val,
                            'significant': p_val < 0.05,
                            'effect_size': np.mean(paired_diff) /
    np.std(paired_diff)
                        }

            # Cognitive load analysis
            cognitive_columns = [col for col in survey_df.columns if
    'cognitive_load' in col]
            if cognitive_columns:
                cognitive_stats = survey_df[cognitive_columns].describe()
                survey_results['cognitive_load_statistics'] =
    cognitive_stats.to_dict()

            # Demographic analysis
            demo_columns = [col for col in survey_df.columns if
    col.startswith('demo_')]
            if demo_columns:
                demo_stats = {}
                for col in demo_columns:
                    if survey_df[col].dtype in ['int64', 'float64']:
                        demo_stats[col] =
    survey_df[col].describe().to_dict()
                    else:
                        demo_stats[col] =
    survey_df[col].value_counts().to_dict()
                survey_results['demographics'] = demo_stats

            return survey_results

        def create_comprehensive_visualizations(self, df: pd.DataFrame, 
                                              survey_df: 
    Optional[pd.DataFrame] = None,
                                              output_dir: str = 
    '../results/') -> None:
            """Create comprehensive visualizations for the study."""
            plt.style.use('seaborn-v0_8')

            # Figure 1: Temporal Evolution Overview
            fig, axes = plt.subplots(2, 2, figsize=(15, 12))

            # 1.1 Causal density over time
            yearly_density = df.groupby('year')['causal_density'].mean()
            axes[0, 0].plot(yearly_density.index, yearly_density.values,
    'b-', linewidth=2)
            axes[0, 0].set_title('Evolution of Causal Density (1950-2025)')
            axes[0, 0].set_xlabel('Year')
            axes[0, 0].set_ylabel('Mean Causal Density')
            axes[0, 0].grid(True, alpha=0.3)

            # 1.2 Category evolution
            categories = ['enablement_foundation_count',
    'inhibition_prevention_count',
                         'statistical_terms_count', 'phraseological_count']
            for category in categories:
                if category in df.columns:
                    yearly_cat = df.groupby('year')[category].mean()
                    axes[0, 1].plot(yearly_cat.index, yearly_cat.values,
                                   label=category.replace('_count',
    '').replace('_', ' ').title())

            axes[0, 1].set_title('Evolution by Category')
            axes[0, 1].set_xlabel('Year')
            axes[0, 1].set_ylabel('Mean Count')
            axes[0, 1].legend()
            axes[0, 1].grid(True, alpha=0.3)

            # 1.3 Decade comparison
            if 'decade' in df.columns:
                sns.boxplot(data=df, x='decade', y='causal_density',
    ax=axes[1, 0])
                axes[1, 0].set_title('Causal Density by Decade')
                axes[1, 0].tick_params(axis='x', rotation=45)

            # 1.4 Subdiscipline comparison
            if 'subdiscipline' in df.columns:
                sns.boxplot(data=df, x='subdiscipline', y='causal_density',
     ax=axes[1, 1])
                axes[1, 1].set_title('Causal Density by Subdiscipline')
                axes[1, 1].tick_params(axis='x', rotation=45)

            plt.tight_layout()

    plt.savefig(f'{output_dir}temporal_evolution_comprehensive.png',
    dpi=300, bbox_inches='tight')
            plt.show()

            # Figure 2: Category Correlation Matrix
            if len([col for col in df.columns if col.endswith('_count')]) >
     1:
                plt.figure(figsize=(10, 8))

                corr_columns = ['causal_density'] + [col for col in
    df.columns if col.endswith('_count')]
                correlation_matrix = df[corr_columns].corr()

                sns.heatmap(correlation_matrix, annot=True, cmap='RdBu_r',
    center=0,
                           square=True, fmt='.3f')
                plt.title('Correlation Matrix: Causal Language Categories')
                plt.tight_layout()
                plt.savefig(f'{output_dir}correlation_matrix.png', dpi=300,
     bbox_inches='tight')
                plt.show()

            # Figure 3: Survey Results (if available)
            if survey_df is not None:
                fig, axes = plt.subplots(2, 2, figsize=(15, 10))

                # Clarity ratings comparison
                clarity_cols = [col for col in survey_df.columns if
    'clarity_rating' in col]
                if clarity_cols:
                    high_density = [col for col in clarity_cols if '_a' in
    col]
                    low_density = [col for col in clarity_cols if '_b' in
    col]

                    if high_density and low_density:
                        high_means = survey_df[high_density].mean()
                        low_means = survey_df[low_density].mean()

                        x = np.arange(len(high_means))
                        width = 0.35

                        axes[0, 0].bar(x - width/2, high_means, width,
    label='High Density', alpha=0.8)
                        axes[0, 0].bar(x + width/2, low_means, width,
    label='Low Density', alpha=0.8)
                        axes[0, 0].set_title('Clarity Ratings: High vs Low 
    Density Abstracts')
                        axes[0, 0].set_ylabel('Mean Rating')
                        axes[0, 0].legend()

                # Cognitive load comparison
                cognitive_cols = [col for col in survey_df.columns if
    'cognitive_load' in col]
                if cognitive_cols:
                    high_cognitive = [col for col in cognitive_cols if '_a'
     in col]
                    low_cognitive = [col for col in cognitive_cols if '_b'
    in col]

                    if high_cognitive and low_cognitive:
                        survey_df[high_cognitive +
    low_cognitive].boxplot(ax=axes[0, 1])
                        axes[0, 1].set_title('Cognitive Load Distribution')
                        axes[0, 1].tick_params(axis='x', rotation=45)

                plt.tight_layout()
                plt.savefig(f'{output_dir}survey_analysis.png', dpi=300,
    bbox_inches='tight')
                plt.show()

        def generate_statistical_report(self, df: pd.DataFrame, 
                                       survey_df: Optional[pd.DataFrame] = 
    None) -> Dict:
            """Generate comprehensive statistical report."""
            report = {
                'study_metadata': {
                    'analysis_date': pd.Timestamp.now().isoformat(),
                    'corpus_size': len(df),
                    'survey_responses': len(survey_df) if survey_df is not
    None else 0
                }
            }

            # Descriptive statistics
            report['descriptive_statistics'] =
    self.descriptive_statistics(df)

            # Temporal trend analysis
            report['temporal_analysis'] = self.temporal_trend_analysis(df)

            # Subdiscipline comparison
            report['subdiscipline_analysis'] =
    self.subdiscipline_comparison(df)

            # Survey analysis
            if survey_df is not None:
                report['survey_analysis'] = self.survey_analysis(survey_df)

            # Statistical tests summary
            significant_trends = []
            for category, stats in
    report['temporal_analysis']['category_trends'].items():
                if stats['significant']:
                    significant_trends.append({
                        'category': category,
                        'trend': stats['trend_direction'],
                        'correlation': stats['correlation'],
                        'p_value': stats['p_value']
                    })

            report['key_findings'] = {
                'significant_temporal_trends': significant_trends,
                'overall_trend_significant':
    report['temporal_analysis']['overall_trend']['p_value'] < 0.05
            }

            return report

        def save_results(self, report: Dict, filename: str = 
    '../results/statistical_analysis_report.json'):
            """Save statistical analysis results."""
            import json

            with open(filename, 'w') as f:
                json.dump(report, f, indent=2, default=str)

            print(f"Statistical analysis report saved to {filename}")

    def main():
        # Example usage with synthetic data
        analyzer = StatisticalAnalyzer()

        # Create synthetic corpus data
        np.random.seed(42)
        n_abstracts = 1000
        years = np.random.choice(range(1950, 2026), n_abstracts)

        # Add temporal trends
        base_density = 3.0
        temporal_effect = (years - 1950) * 0.02  # Slight increase over 
    time

        corpus_data = pd.DataFrame({
            'year': years,
            'decade': ['1950s' if y < 1960 else '1960s' if y < 1970 else
    '1970s' if y < 1980 else
                      '1980s' if y < 1990 else '1990s' if y < 2000 else
    '2000s' if y < 2010 else
                      '2010s' if y < 2020 else '2020s' for y in years],
            'causal_density': np.random.exponential(base_density) +
    temporal_effect + np.random.normal(0, 0.5, n_abstracts),
            'total_causal_terms': np.random.poisson(5, n_abstracts),
            'enablement_foundation_count': np.random.poisson(2,
    n_abstracts),
            'inhibition_prevention_count': np.random.poisson(1,
    n_abstracts),
            'statistical_terms_count': np.random.poisson(1, n_abstracts) +
    (years - 1950) * 0.01,
            'phraseological_count': np.random.poisson(1.5, n_abstracts),
            'subdiscipline': np.random.choice(['Ethics', 'Epistemology',
    'Philosophy of Science',
                                             'Metaphysics', 'Philosophy of 
    Mind'], n_abstracts)
        })

        # Create synthetic survey data
        n_responses = 350
        survey_data = pd.DataFrame({
            'demo_age': np.random.normal(35, 12, n_responses),
            'demo_education': np.random.choice(['Bachelor\'s degree',
    'Master\'s degree', 'Doctoral degree'], n_responses),
            'abstract_pair_1_clarity_rating_a': np.random.choice(range(1,
    6), n_responses),
            'abstract_pair_1_clarity_rating_b': np.random.choice(range(2,
    6), n_responses),  # Slightly higher for low density
            'abstract_pair_1_cognitive_load_a': np.random.choice(range(2,
    6), n_responses),
            'abstract_pair_1_cognitive_load_b': np.random.choice(range(1,
    5), n_responses),  # Lower cognitive load for low density
        })

        # Run analysis
        report = analyzer.generate_statistical_report(corpus_data,
    survey_data)
        analyzer.create_comprehensive_visualizations(corpus_data,
    survey_data)
        analyzer.save_results(report)

        print("Statistical Analysis Complete!")
        print(f"Key Findings:")
        print(f"- Significant temporal trends: 
    {len(report['key_findings']['significant_temporal_trends'])}")
        print(f"- Overall trend significant: 
    {report['key_findings']['overall_trend_significant']}")

    if __name__ == "__main__":
        main()


