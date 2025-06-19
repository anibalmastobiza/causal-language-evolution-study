 import requests
    import pandas as pd
    import time
    from typing import Dict, List, Optional
    from abc import ABC, abstractmethod
    import json
    from urllib.parse import urlencode
    import xml.etree.ElementTree as ET

    class AbstractCollector(ABC):
        """Abstract base class for different data source collectors."""

        @abstractmethod
        def search_abstracts(self, query: str, year_range: tuple, limit: 
    int) -> List[Dict]:
            pass

        @abstractmethod
        def format_abstract_data(self, raw_data: Dict) -> Dict:
            pass

    class CrossRefCollector(AbstractCollector):
        """Collector for CrossRef API - open access academic papers."""

        def __init__(self, email: str):
            self.base_url = "https://api.crossref.org/works"
            self.email = email
            self.headers = {'User-Agent': f'PhilosophyStudy/1.0 
    (mailto:{email})'}

        def search_abstracts(self, query: str, year_range: tuple, limit: 
    int = 1000) -> List[Dict]:
            """Search CrossRef for philosophical abstracts."""
            abstracts = []
            offset = 0
            per_page = 100

            while len(abstracts) < limit:
                params = {
                    'query': f'{query} philosophy',
                    'filter': f'from-pub-date:{year_range[0]},until-pub-dat
    e:{year_range[1]},type:journal-article',
                    'rows': per_page,
                    'offset': offset,
                    'select': 'title,abstract,published-print,published-onl
    ine,subject,container-title,author'
                }

                try:
                    response = requests.get(self.base_url, params=params,
    headers=self.headers)
                    response.raise_for_status()

                    data = response.json()
                    items = data.get('message', {}).get('items', [])

                    if not items:
                        break

                    for item in items:
                        if 'abstract' in item and item['abstract']:
                            formatted = self.format_abstract_data(item)
                            if formatted:
                                abstracts.append(formatted)

                    offset += per_page
                    time.sleep(1)  # Rate limiting

                except Exception as e:
                    print(f"Error fetching from CrossRef: {e}")
                    break

            return abstracts[:limit]

        def format_abstract_data(self, raw_data: Dict) -> Optional[Dict]:
            """Format CrossRef data into standardized format."""
            try:
                # Extract publication year
                pub_date = raw_data.get('published-print') or
    raw_data.get('published-online')
                if not pub_date or 'date-parts' not in pub_date:
                    return None

                year = pub_date['date-parts'][0][0]

                # Check if it's philosophy-related
                subjects = raw_data.get('subject', [])
                container_title = raw_data.get('container-title',
    [''])[0].lower()

                philosophy_keywords = ['philosophy', 'philosophical',
    'ethics', 'epistemology',
                                     'metaphysics', 'logic', 'moral',
    'political philosophy']

                is_philosophy = any(keyword in container_title for keyword
    in philosophy_keywords) or \
                               any(keyword in ' '.join(subjects).lower()
    for keyword in philosophy_keywords)

                if not is_philosophy:
                    return None

                return {
                    'title': ' '.join(raw_data.get('title', [])),
                    'abstract': raw_data.get('abstract', '').strip(),
                    'year': year,
                    'journal': raw_data.get('container-title', [''])[0],
                    'authors': [f"{author.get('given', '')} 
    {author.get('family', '')}"
                               for author in raw_data.get('author', [])],
                    'subjects': subjects,
                    'source': 'CrossRef',
                    'subdiscipline':
    self._classify_subdiscipline(raw_data.get('abstract', ''), subjects)
                }
            except Exception as e:
                print(f"Error formatting CrossRef data: {e}")
                return None

        def _classify_subdiscipline(self, abstract: str, subjects: 
    List[str]) -> str:
            """Classify philosophical subdiscipline based on content."""
            abstract_lower = abstract.lower()
            subjects_text = ' '.join(subjects).lower()

            subdiscipline_keywords = {
                'Ethics': ['ethics', 'moral', 'virtue', 'duty', 'rights',
    'justice', 'bioethics'],
                'Epistemology': ['knowledge', 'belief', 'justification',
    'skepticism', 'evidence'],
                'Philosophy of Science': ['science', 'scientific',
    'causation', 'explanation', 'theory'],
                'Metaphysics': ['being', 'existence', 'reality',
    'substance', 'property', 'time'],
                'Philosophy of Mind': ['mind', 'consciousness', 'mental',
    'cognitive', 'intentionality'],
                'Political Philosophy': ['political', 'democracy', 'state',
     'power', 'authority'],
                'Logic': ['logic', 'reasoning', 'argument', 'inference',
    'validity']
            }

            for subdiscipline, keywords in subdiscipline_keywords.items():
                if any(keyword in abstract_lower or keyword in
    subjects_text
                       for keyword in keywords):
                    return subdiscipline

            return 'General Philosophy'

    class PhilPapersCollector(AbstractCollector):
        """Collector for PhilPapers (simulated - would need API access)."""

        def search_abstracts(self, query: str, year_range: tuple, limit: 
    int = 1000) -> List[Dict]:
            """Simulate PhilPapers collection - in practice would use their
     API."""
            print("PhilPapers collector would require institutional access 
    or API key")
            return []

        def format_abstract_data(self, raw_data: Dict) -> Dict:
            return raw_data

    class CorpusManager:
        """Main corpus collection and management system."""

        def __init__(self, email: str):
            self.collectors = {
                'crossref': CrossRefCollector(email),


⏺ Read(file_path: "/Users/anibalmonasterioastobiza/causal-language-evolutio
      n-study/src/corpus_collector.py", offset: 150, limit: 150)
  ⎿             'crossref': CrossRefCollector(email),                      
                'philpapers': PhilPapersCollector()
            }
            self.collected_abstracts = []

        def collect_corpus(self, sources: List[str] = ['crossref'], 
                          year_range: tuple = (1950, 2025), 
                          abstracts_per_source: int = 1000) -> 
    pd.DataFrame:
            """Collect abstracts from multiple sources."""
            all_abstracts = []

            philosophy_queries = [
                "philosophical analysis", "ethical theory",
    "epistemological",
                "metaphysical", "philosophy of mind", "political 
    philosophy",
                "philosophy of science", "moral philosophy"
            ]

            for source in sources:
                if source not in self.collectors:
                    print(f"Unknown source: {source}")
                    continue

                collector = self.collectors[source]
                print(f"Collecting from {source}...")

                for query in philosophy_queries:
                    try:
                        abstracts = collector.search_abstracts(
                            query, year_range, abstracts_per_source //
    len(philosophy_queries)
                        )
                        all_abstracts.extend(abstracts)
                        print(f"Collected {len(abstracts)} abstracts for 
    query: {query}")
                        time.sleep(2)  # Rate limiting between queries
                    except Exception as e:
                        print(f"Error collecting from {source} with query 
    '{query}': {e}")

            # Remove duplicates based on title and abstract similarity
            unique_abstracts = self._remove_duplicates(all_abstracts)

            # Convert to DataFrame
            df = pd.DataFrame(unique_abstracts)

            # Additional filtering and cleaning
            if not df.empty:
                df = self._clean_corpus(df)

            self.collected_abstracts = unique_abstracts
            return df

        def _remove_duplicates(self, abstracts: List[Dict]) -> List[Dict]:
            """Remove duplicate abstracts based on title similarity."""
            unique_abstracts = []
            seen_titles = set()

            for abstract in abstracts:
                title_lower = abstract.get('title', '').lower().strip()
                if title_lower and title_lower not in seen_titles:
                    seen_titles.add(title_lower)
                    unique_abstracts.append(abstract)

            return unique_abstracts

        def _clean_corpus(self, df: pd.DataFrame) -> pd.DataFrame:
            """Clean and validate corpus data."""
            # Remove entries with missing essential data
            df = df.dropna(subset=['title', 'abstract', 'year'])

            # Filter by abstract length (remove too short/long)
            df = df[df['abstract'].str.len().between(100, 2000)]

            # Ensure year is within range
            df = df[df['year'].between(1950, 2025)]

            # Clean text
            df['abstract'] = df['abstract'].str.replace(r'\s+', ' ',
    regex=True)
            df['title'] = df['title'].str.replace(r'\s+', ' ', regex=True)

            return df.reset_index(drop=True)

        def save_corpus(self, df: pd.DataFrame, filename: str = 
    '../data/philosophical_abstracts_corpus.csv'):
            """Save collected corpus to file."""
            df.to_csv(filename, index=False)
            print(f"Corpus saved to {filename}")

            # Save metadata
            metadata = {
                'total_abstracts': len(df),
                'year_range': (df['year'].min(), df['year'].max()),
                'sources': df['source'].unique().tolist(),
                'subdisciplines':
    df['subdiscipline'].value_counts().to_dict(),
                'collection_date': pd.Timestamp.now().isoformat()
            }

            with open(filename.replace('.csv', '_metadata.json'), 'w') as
    f:
                json.dump(metadata, f, indent=2)

        def load_corpus(self, filename: str = 
    '../data/philosophical_abstracts_corpus.csv') -> pd.DataFrame:
            """Load previously collected corpus."""
            try:
                df = pd.read_csv(filename)
                print(f"Loaded corpus with {len(df)} abstracts")
                return df
            except FileNotFoundError:
                print(f"Corpus file {filename} not found")
                return pd.DataFrame()

    def main():
        # Example usage
        manager = CorpusManager(email="researcher@example.com")

        # Collect corpus (would need API access for real data)
        corpus_df = manager.collect_corpus(
            sources=['crossref'],
            year_range=(2020, 2025),  # Start with recent years for testing
            abstracts_per_source=100
        )

        if not corpus_df.empty:
            print(f"Collected {len(corpus_df)} abstracts")
            print(f"Year range: {corpus_df['year'].min()} - 
    {corpus_df['year'].max()}")
            print(f"Subdisciplines: 
    {corpus_df['subdiscipline'].value_counts().to_dict()}")

            # Save corpus
            manager.save_corpus(corpus_df)
        else:
            print("No abstracts collected")

    if __name__ == "__main__":
        main()

