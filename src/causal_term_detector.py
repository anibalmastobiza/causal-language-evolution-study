 import re
    import pandas as pd
    from typing import Dict, List, Tuple
    from collections import defaultdict

    class CausalTermDetector:
        def __init__(self):
            self.causal_categories = {
                'enablement_foundation': [
                    'posibilitar', 'subyacer', 'sustentar', 'presuponer',
    'enable', 'underlie',
                    'sustain', 'presuppose', 'facilitate', 'allow',
    'permit', 'make possible',
                    'ground', 'support', 'foundation', 'basis',
    'fundamental'
                ],
                'inhibition_prevention': [
                    'impedir', 'inhibir', 'limitar', 'obstaculizar',
    'atenuar', 'prevent',
                    'inhibit', 'limit', 'obstruct', 'hinder', 'block',
    'restrict', 'constrain',
                    'diminish', 'reduce', 'weaken', 'suppress'
                ],
                'reciprocal_causal': [
                    'retroalimentarse', 'interactuar', 'relación 
    dialéctica', 'feedback',
                    'interact', 'dialectical relationship', 'mutual 
    influence', 'reciprocal',
                    'bidirectional', 'circular causation', 'loop',
    'interdependence'
                ],
                'phraseological': [
                    'piedra angular', 'sentar bases', 'catalizador',
    'traducirse en',
                    'desempeñar papel', 'función de', 'guardar relación 
    directa',
                    'cornerstone', 'lay foundation', 'catalyst', 'translate
     into',
                    'play role', 'function of', 'direct relationship',
    'inverse relationship',
                    'key factor', 'driving force', 'crucial element'
                ],
                'statistical_terms': [
                    'predecir', 'explicar varianza', 'predictor 
    significativo', 'efecto significativo',
                    'predict', 'explain variance', 'significant predictor',
     'significant effect',
                    'correlation', 'regression', 'model', 'coefficient',
    'p-value',
                    'statistical significance', 'confidence interval'
                ],
                'mediation_moderation': [
                    'mediación', 'moderación', 'variable mediadora',
    'variable moderadora',
                    'mediation', 'moderation', 'mediating variable',
    'moderating variable',
                    'indirect effect', 'conditional effect', 'interaction 
    effect',
                    'pathway', 'mechanism', 'intervening variable'
                ]
            }

            # Compile regex patterns for efficient matching
            self.compiled_patterns = {}
            for category, terms in self.causal_categories.items():
                pattern = r'\b(?:' + '|'.join(re.escape(term) for term in
    terms) + r')\b'
                self.compiled_patterns[category] = re.compile(pattern,
    re.IGNORECASE)

        def detect_causal_terms(self, text: str) -> Dict[str, List[str]]:
            """Detect causal terms in text and categorize them."""
            detected = defaultdict(list)

            for category, pattern in self.compiled_patterns.items():
                matches = pattern.findall(text)
                if matches:
                    detected[category].extend(matches)

            return dict(detected)

        def calculate_causal_density(self, text: str) -> float:
            """Calculate density of causal terms per 100 words."""
            word_count = len(text.split())
            total_causal_terms = sum(len(terms) for terms in
    self.detect_causal_terms(text).values())
            return (total_causal_terms / word_count) * 100 if word_count >
    0 else 0

        def analyze_corpus(self, abstracts_df: pd.DataFrame, text_column: 
    str = 'abstract', 
                          year_column: str = 'year') -> pd.DataFrame:
            """Analyze entire corpus of abstracts."""
            results = []

            for idx, row in abstracts_df.iterrows():
                text = row[text_column]
                year = row[year_column]

                detected_terms = self.detect_causal_terms(text)
                density = self.calculate_causal_density(text)

                result = {
                    'id': idx,
                    'year': year,
                    'text': text,
                    'causal_density': density,
                    'total_causal_terms': sum(len(terms) for terms in
    detected_terms.values())
                }

                # Add counts for each category
                for category in self.causal_categories.keys():
                    result[f'{category}_count'] =
    len(detected_terms.get(category, []))
                    result[f'{category}_terms'] =
    detected_terms.get(category, [])

                results.append(result)

            return pd.DataFrame(results)

    def main():
        # Example usage
        detector = CausalTermDetector()

        # Sample philosophical abstract
        sample_text = """
        This article sustains that neural plasticity underlies higher 
    cognitive processes, 
        enabling complex interactions that play a crucial role in memory 
    formation. 
        The statistical analysis reveals significant predictors and 
    explains variance 
        in cognitive performance through mediating variables.
        """

        detected = detector.detect_causal_terms(sample_text)
        density = detector.calculate_causal_density(sample_text)

        print("Detected causal terms:")
        for category, terms in detected.items():
            print(f"  {category}: {terms}")
        print(f"Causal density: {density:.2f} terms per 100 words")

    if __name__ == "__main__":
        main()

