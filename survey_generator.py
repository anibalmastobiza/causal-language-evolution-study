import random                                                            │ │
│ │ import json                                                              │ │
│ │ from typing import Dict, List, Tuple                                     │ │
│ │ from dataclasses import dataclass                                        │ │
│ │                                                                          │ │
│ │ @dataclass                                                               │ │
│ │ class AbstractTemplate:                                                  │ │
│ │     topic: str                                                           │ │
│ │     base_text: str                                                       │ │
│ │     high_density_terms: List[str]                                        │ │
│ │     low_density_alternatives: List[str]                                  │ │
│ │                                                                          │ │
│ │ class AbstractGenerator:                                                 │ │
│ │     def __init__(self):                                                  │ │
│ │         self.causal_terms = {                                            │ │
│ │             'enablement_foundation': [                                   │ │
│ │                 'sustains', 'underlies', 'enables', 'facilitates',       │ │
│ │ 'grounds',                                                               │ │
│ │                 'presupposes', 'supports', 'forms the foundation',       │ │
│ │ 'serves as basis',                                                       │ │
│ │                 'provides the groundwork', 'establishes the framework'   │ │
│ │             ],                                                           │ │
│ │             'inhibition_prevention': [                                   │ │
│ │                 'inhibits', 'prevents', 'constrains', 'limits',          │ │
│ │ 'blocks',                                                                │ │
│ │                 'hinders', 'restricts', 'impedes', 'obstructs',          │ │
│ │ 'diminishes'                                                             │ │
│ │             ],                                                           │ │
│ │             'reciprocal_causal': [                                       │ │
│ │                 'reciprocal processes', 'dialectical relationship',      │ │
│ │ 'bidirectional effects',                                                 │ │
│ │                 'mutual influence', 'feedback loops', 'circular          │ │
│ │ causation',                                                              │ │
│ │                 'interdependent mechanisms', 'interactive dynamics'      │ │
│ │             ],                                                           │ │
│ │             'phraseological': [                                          │ │
│ │                 'cornerstone', 'catalyst', 'driving force', 'key         │ │
│ │ factor',                                                                 │ │
│ │                 'crucial element', 'plays a pivotal role', 'serves as',  │ │
│ │                 'functions as', 'translates into', 'gives rise to'       │ │
│ │             ],                                                           │ │
│ │             'statistical_terms': [                                       │ │
│ │                 'significant predictor', 'explains variance', 'mediating │ │
│ │  variable',                                                              │ │
│ │                 'moderating effect', 'statistical significance',         │ │
│ │ 'correlation',                                                           │ │
│ │                 'regression analysis reveals', 'predictive model'        │ │
│ │             ],                                                           │ │
│ │             'mediation_moderation': [                                    │ │
│ │                 'mediating pathways', 'indirect effects', 'moderating    │ │
│ │ factors',                                                                │ │
│ │                 'intervening mechanisms', 'conditional effects',         │ │
│ │ 'pathway analysis'                                                       │ │
│ │             ]                                                            │ │
│ │         }                                                                │ │
│ │                                                                          │ │
│ │         self.neutral_alternatives = {                                    │ │
│ │             'sustains': 'shows', 'underlies': 'relates to', 'enables':   │ │
│ │ 'allows',                                                                │ │
│ │             'inhibits': 'affects', 'prevents': 'reduces', 'constrains':  │ │
│ │ 'influences',                                                            │ │
│ │             'reciprocal processes': 'processes', 'dialectical            │ │
│ │ relationship': 'relationship',                                           │ │
│ │             'cornerstone': 'element', 'catalyst': 'factor', 'significant │ │
│ │  predictor': 'factor',                                                   │ │
│ │             'mediating pathways': 'pathways', 'indirect effects':        │ │
│ │ 'effects'                                                                │ │
│ │         }                                                                │ │
│ │                                                                          │ │
│ │         self.abstract_templates = self._create_abstract_templates()      │ │
│ │                                                                          │ │
│ │     def _create_abstract_templates(self) -> List[AbstractTemplate]:      │ │
│ │         """Create diverse philosophical abstract templates."""           │ │
│ │         return [                                                         │ │
│ │             AbstractTemplate(                                            │ │
│ │                 topic="Consciousness and Free Will",                     │ │
│ │                 base_text="This investigation examines the relationship  │ │
│ │ between consciousness and free will in moral decision-making. The        │ │
│ │ research explores how cognitive processes contribute to autonomous       │ │
│ │ choice. Analysis demonstrates connections between neural activity and    │ │
│ │ ethical reasoning through various pathways.",                            │ │
│ │                 high_density_terms=[                                     │ │
│ │                     "sustains that consciousness", "underlies moral      │ │
│ │ agency", "enables autonomous choice",                                    │ │
│ │                     "mediating pathways", "serves as the cornerstone",   │ │
│ │ "reciprocal processes",                                                  │ │
│ │                     "significant predictor of", "translates into         │ │
│ │ behavioral outcomes"                                                     │ │
│ │                 ],                                                       │ │
│ │                 low_density_alternatives=[                               │ │
│ │                     "shows that consciousness", "relates to moral        │ │
│ │ agency", "allows autonomous choice",                                     │ │
│ │                     "pathways", "important element", "processes",        │ │
│ │                     "factor in", "leads to behavioral outcomes"          │ │
│ │                 ]                                                        │ │
│ │             ),                                                           │ │
│ │                                                                          │ │
│ │             AbstractTemplate(                                            │ │
│ │                 topic="Artificial Intelligence Ethics",                  │ │
│ │                 base_text="This study analyzes ethical frameworks for    │ │
│ │ artificial intelligence development. The research investigates how moral │ │
│ │  principles apply to algorithmic decision-making. Results show           │ │
│ │ relationships between computational processes and ethical considerations │ │
│ │  through systematic analysis.",                                          │ │
│ │                 high_density_terms=[                                     │ │
│ │                     "underlies ethical reasoning", "facilitates moral    │ │
│ │ judgment", "constrains algorithmic bias",                                │ │
│ │                     "dialectical relationship", "functions as catalyst", │ │
│ │  "mediating variables",                                                  │ │
│ │                     "explains variance in", "inhibits discriminatory     │ │
│ │ outcomes"                                                                │ │
│ │                 ],                                                       │ │
│ │                 low_density_alternatives=[                               │ │
│ │                     "relates to ethical reasoning", "supports moral      │ │
│ │ judgment", "reduces algorithmic bias",                                   │ │
│ │                     "relationship", "acts as factor", "variables",       │ │
│ │                     "accounts for variation in", "reduces discriminatory │ │
│ │  outcomes"                                                               │ │
│ │                 ]                                                        │ │
│ │             ),                                                           │ │
│ │                                                                          │ │
│ │             AbstractTemplate(                                            │ │
│ │                 topic="Knowledge and Belief",                            │ │
│ │                 base_text="This article explores the epistemological     │ │
│ │ distinction between knowledge and belief in scientific contexts. The     │ │
│ │ study examines how evidential reasoning contributes to knowledge         │ │
│ │ formation. Findings reveal connections between justification processes   │ │
│ │ and truth conditions.",                                                  │ │
│ │                 high_density_terms=[                                     │ │
│ │                     "presupposes evidential grounding", "enables         │ │
│ │ knowledge acquisition", "sustains belief formation",                     │ │
│ │                     "reciprocal feedback", "cornerstone of               │ │
│ │ epistemology", "mediating role of",                                      │ │
│ │                     "predictive model shows", "gives rise to justified   │ │
│ │ belief"                                                                  │ │
│ │                 ],                                                       │ │
│ │                 low_density_alternatives=[                               │ │
│ │                     "involves evidential grounding", "supports knowledge │ │
│ │  acquisition", "shows belief formation",                                 │ │
│ │                     "feedback", "central to epistemology", "role of",    │ │
│ │                     "model shows", "results in justified belief"         │ │
│ │                 ]                                                        │ │
│ │             ),                                                           │ │
│ │                                                                          │ │
│ │             AbstractTemplate(                                            │ │
│ │                 topic="Social Justice Theory",                           │ │
│ │                 base_text="This research examines distributive justice   │ │
│ │ principles in contemporary political philosophy. The analysis            │ │
│ │ investigates how institutional frameworks affect social equality. The    │ │
│ │ study explores relationships between policy mechanisms and equitable     │ │
│ │ outcomes.",                                                              │ │
│ │                 high_density_terms=[                                     │ │
│ │                     "underlies distributive fairness", "facilitates      │ │
│ │ social equity", "constrains inequality",                                 │ │
│ │                     "bidirectional causation", "driving force behind",   │ │
│ │ "indirect effects of",                                                   │ │
│ │                     "regression analysis reveals", "moderating influence │ │
│ │  on"                                                                     │ │
│ │                 ],                                                       │ │
│ │                 low_density_alternatives=[                               │ │
│ │                     "supports distributive fairness", "promotes social   │ │
│ │ equity", "reduces inequality",                                           │ │
│ │                     "causation", "important factor in", "effects of",    │ │
│ │                     "analysis reveals", "influence on"                   │ │
│ │                 ]                                                        │ │
│ │             ),                                                           │ │
│ │                                                                          │ │
│ │             AbstractTemplate(                                            │ │
│ │                 topic="Moral Psychology",                                │ │
│ │                 base_text="This investigation analyzes the psychological │ │
│ │  foundations of moral reasoning across cultures. The research examines   │ │
│ │ how emotional responses relate to ethical judgments. Results demonstrate │ │
│ │  patterns in the relationship between affect and moral cognition.",      │ │
│ │                 high_density_terms=[                                     │ │
│ │                     "grounds moral intuition", "enables ethical          │ │
│ │ reasoning", "sustains cultural values",                                  │ │
│ │                     "circular causation between", "serves as catalyst    │ │
│ │ for", "mediating pathways",                                              │ │
│ │                     "significant correlation with", "translates into     │ │
│ │ moral behavior"                                                          │ │
│ │                 ],                                                       │ │
│ │                 low_density_alternatives=[                               │ │
│ │                     "supports moral intuition", "aids ethical            │ │
│ │ reasoning", "maintains cultural values",                                 │ │
│ │                     "relationship between", "factor for", "pathways",    │ │
│ │                     "correlation with", "leads to moral behavior"        │ │
│ │                 ]                                                        │ │
│ │             ),                                                           │ │
│ │                                                                          │ │
│ │             AbstractTemplate(                                            │ │
│ │                 topic="Philosophy of Mind",                              │ │
│ │                 base_text="This study investigates the relationship      │ │
│ │ between mental states and physical processes in cognitive science. The   │ │
│ │ research explores how neural mechanisms relate to conscious experience.  │ │
│ │ Analysis examines connections between brain activity and subjective      │ │
│ │ phenomena.",                                                             │ │
│ │                 high_density_terms=[                                     │ │
│ │                     "underlies conscious experience", "facilitates       │ │
│ │ mental representation", "constrains cognitive processing",               │ │
│ │                     "reciprocal interactions", "foundational to",        │ │
│ │ "conditional effects of",                                                │ │
│ │                     "explains variance in consciousness", "inhibits      │ │
│ │ reductive explanations"                                                  │ │
│ │                 ],                                                       │ │
│ │                 low_density_alternatives=[                               │ │
│ │                     "relates to conscious experience", "supports mental  │ │
│ │ representation", "affects cognitive processing",                         │ │
│ │                     "interactions", "important for", "effects of",       │ │
│ │                     "variation in consciousness", "challenges reductive  │ │
│ │ explanations"                                                            │ │
│ │                 ]                                                        │ │
│ │             ),                                                           │ │
│ │                                                                          │ │
│ │             AbstractTemplate(                                            │ │
│ │                 topic="Environmental Ethics",                            │ │
│ │                 base_text="This research examines moral obligations      │ │
│ │ toward future generations in environmental policy. The study             │ │
│ │ investigates how sustainability principles apply to resource management. │ │
│ │  Findings reveal relationships between ethical frameworks and            │ │
│ │ conservation practices.",                                                │ │
│ │                 high_density_terms=[                                     │ │
│ │                     "presupposes intergenerational duty", "enables       │ │
│ │ sustainable practice", "grounds environmental responsibility",           │ │
│ │                     "dialectical tension", "cornerstone of               │ │
│ │ sustainability", "mediating role",                                       │ │
│ │                     "predictive indicators of", "gives rise to           │ │
│ │ conservation behavior"                                                   │ │
│ │                 ],                                                       │ │
│ │                 low_density_alternatives=[                               │ │
│ │                     "involves intergenerational duty", "supports         │ │
│ │ sustainable practice", "basis for environmental responsibility",         │ │
│ │                     "tension", "central to sustainability", "role",      │ │
│ │                     "indicators of", "results in conservation behavior"  │ │
│ │                 ]                                                        │ │
│ │             ),                                                           │ │
│ │                                                                          │ │
│ │             AbstractTemplate(                                            │ │
│ │                 topic="Philosophy of Language",                          │ │
│ │                 base_text="This investigation analyzes the relationship  │ │
│ │ between meaning and context in linguistic communication. The research    │ │
│ │ examines how pragmatic factors influence semantic interpretation. The    │ │
│ │ study explores connections between speaker intention and listener        │ │
│ │ comprehension.",                                                         │ │
│ │                 high_density_terms=[                                     │ │
│ │                     "underlies semantic content", "facilitates           │ │
│ │ linguistic understanding", "constrains interpretation",                  │ │
│ │                     "feedback mechanisms", "driving force in             │ │
│ │ communication", "indirect pathways",                                     │ │
│ │                     "correlation analysis shows", "moderates             │ │
│ │ comprehension processes"                                                 │ │
│ │                 ],                                                       │ │
│ │                 low_density_alternatives=[                               │ │
│ │                     "relates to semantic content", "aids linguistic      │ │
│ │ understanding", "affects interpretation",                                │ │
│ │                     "mechanisms", "factor in communication", "pathways", │ │
│ │                     "analysis shows", "influences comprehension          │ │
│ │ processes"                                                               │ │
│ │                 ]                                                        │ │
│ │             ),                                                           │ │
│ │                                                                          │ │
│ │             AbstractTemplate(                                            │ │
│ │                 topic="Political Philosophy",                            │ │
│ │                 base_text="This study examines democratic legitimacy in  │ │
│ │ pluralistic societies. The research investigates how institutional       │ │
│ │ design affects political representation. Analysis explores relationships │ │
│ │  between governance structures and citizen participation.",              │ │
│ │                 high_density_terms=[                                     │ │
│ │                     "sustains democratic legitimacy", "enables political │ │
│ │  representation", "facilitates civic engagement",                        │ │
│ │                     "reciprocal relationship", "serves as foundation",   │ │
│ │ "mediating institutions",                                                │ │
│ │                     "significant predictors of participation",           │ │
│ │ "translates into democratic outcomes"                                    │ │
│ │                 ],                                                       │ │
│ │                 low_density_alternatives=[                               │ │
│ │                     "supports democratic legitimacy", "allows political  │ │
│ │ representation", "promotes civic engagement",                            │ │
│ │                     "relationship", "acts as foundation",                │ │
│ │ "institutions",                                                          │ │
│ │                     "predictors of participation", "leads to democratic  │ │
│ │ outcomes"                                                                │ │
│ │                 ]                                                        │ │
│ │             ),                                                           │ │
│ │                                                                          │ │
│ │             AbstractTemplate(                                            │ │
│ │                 topic="Philosophy of Science",                           │ │
│ │                 base_text="This research analyzes the role of scientific │ │
│ │  models in theoretical understanding. The study examines how             │ │
│ │ representational structures contribute to scientific explanation.        │ │
│ │ Findings demonstrate patterns in the relationship between models and     │ │
│ │ empirical adequacy.",                                                    │ │
│ │                 high_density_terms=[                                     │ │
│ │                     "underlies theoretical representation", "enables     │ │
│ │ scientific understanding", "grounds explanatory power",                  │ │
│ │                     "bidirectional validation", "cornerstone of          │ │
│ │ scientific method", "conditional mechanisms",                            │ │
│ │                     "regression models indicate", "inhibits theoretical  │ │
│ │ reduction"                                                               │ │
│ │                 ],                                                       │ │
│ │                 low_density_alternatives=[                               │ │
│ │                     "supports theoretical representation", "aids         │ │
│ │ scientific understanding", "basis for explanatory power",                │ │
│ │                     "validation", "central to scientific method",        │ │
│ │ "mechanisms",                                                            │ │
│ │                     "models indicate", "challenges theoretical           │ │
│ │ reduction"                                                               │ │
│ │                 ]                                                        │ │
│ │             )                                                            │ │
│ │         ]                                                                │ │
│ │                                                                          │ │
│ │     def generate_abstract_pair(self) -> Tuple[Dict, Dict]:               │ │
│ │         """Generate a randomized pair of high and low density            │ │
│ │ abstracts."""                                                            │ │
│ │         template = random.choice(self.abstract_templates)                │ │
│ │                                                                          │ │
│ │         # Generate high density version                                  │ │
│ │         high_density = self._create_high_density_abstract(template)      │ │
│ │                                                                          │ │
│ │         # Generate low density version                                   │ │
│ │         low_density = self._create_low_density_abstract(template)        │ │
│ │                                                                          │ │
│ │         return high_density, low_density                                 │ │
│ │                                                                          │ │
│ │     def _create_high_density_abstract(self, template: AbstractTemplate)  │ │
│ │ -> Dict:                                                                 │ │
│ │         """Create high causal density abstract from template."""         │ │
│ │         # Replace base terms with high density causal terms              │ │
│ │         text = template.base_text                                        │ │
│ │                                                                          │ │
│ │         # Add causal terms strategically                                 │ │
│ │         sentences = text.split('. ')                                     │ │
│ │         enhanced_sentences = []                                          │ │
│ │                                                                          │ │
│ │         for i, sentence in enumerate(sentences):                         │ │
│ │             if i < len(template.high_density_terms):                     │ │
│ │                 # Insert causal term                                     │ │
│ │                 causal_term = template.high_density_terms[i]             │ │
│ │                 # Find a suitable insertion point                        │ │
│ │                 words = sentence.split()                                 │ │
│ │                 if len(words) > 5:                                       │ │
│ │                     insertion_point = len(words) // 2                    │ │
│ │                     words.insert(insertion_point, causal_term)           │ │
│ │                     sentence = ' '.join(words)                           │ │
│ │             enhanced_sentences.append(sentence)                          │ │
│ │                                                                          │ │
│ │         enhanced_text = '. '.join(enhanced_sentences)                    │ │
│ │                                                                          │ │
│ │         # Calculate density                                              │ │
│ │         density = self._calculate_density(enhanced_text)                 │ │
│ │                                                                          │ │
│ │         return {                                                         │ │
│ │             'id': f'hd_{template.topic.lower().replace(" ",              │ │
│ │ "_")}_{random.randint(1000, 9999)}',                                     │ │
│ │             'text': enhanced_text,                                       │ │
│ │             'topic': template.topic,                                     │ │
│ │             'density': density,                                          │ │
│ │             'type': 'high_density'                                       │ │
│ │         }                                                                │ │
│ │                                                                          │ │
│ │     def _create_low_density_abstract(self, template: AbstractTemplate)   │ │
│ │ -> Dict:                                                                 │ │
│ │         """Create low causal density abstract from template."""          │ │
│ │         text = template.base_text                                        │ │
│ │                                                                          │ │
│ │         # Replace any existing causal terms with neutral alternatives    │ │
│ │         for causal_term, neutral_term in                                 │ │
│ │ self.neutral_alternatives.items():                                       │ │
│ │             text = text.replace(causal_term, neutral_term)               │ │
│ │                                                                          │ │
│ │         # Use low density alternatives                                   │ │
│ │         sentences = text.split('. ')                                     │ │
│ │         enhanced_sentences = []                                          │ │
│ │                                                                          │ │
│ │         for i, sentence in enumerate(sentences):                         │ │
│ │             if i < len(template.low_density_alternatives):               │ │
│ │                 alt_term = template.low_density_alternatives[i]          │ │
│ │                 words = sentence.split()                                 │ │
│ │                 if len(words) > 5:                                       │ │
│ │                     insertion_point = len(words) // 2                    │ │
│ │                     words.insert(insertion_point, alt_term)              │ │
│ │                     sentence = ' '.join(words)                           │ │
│ │             enhanced_sentences.append(sentence)                          │ │
│ │                                                                          │ │
│ │         enhanced_text = '. '.join(enhanced_sentences)                    │ │
│ │         density = self._calculate_density(enhanced_text)                 │ │
│ │                                                                          │ │
│ │         return {                                                         │ │
│ │             'id': f'ld_{template.topic.lower().replace(" ",              │ │
│ │ "_")}_{random.randint(1000, 9999)}',                                     │ │
│ │             'text': enhanced_text,                                       │ │
│ │             'topic': template.topic,                                     │ │
│ │             'density': density,                                          │ │
│ │             'type': 'low_density'                                        │ │
│ │         }                                                                │ │
│ │                                                                          │ │
│ │     def _calculate_density(self, text: str) -> float:                    │ │
│ │         """Calculate causal term density per 100 words."""               │ │
│ │         words = len(text.split())                                        │ │
│ │         causal_count = 0                                                 │ │
│ │                                                                          │ │
│ │         text_lower = text.lower()                                        │ │
│ │         for category_terms in self.causal_terms.values():                │ │
│ │             for term in category_terms:                                  │ │
│ │                 causal_count += text_lower.count(term.lower())           │ │
│ │                                                                          │ │
│ │         return (causal_count / words) * 100 if words > 0 else 0          │ │
│ │                                                                          │ │
│ │     def generate_multiple_pairs(self, n_pairs: int = 20) ->              │ │
│ │ List[Tuple[Dict, Dict]]:                                                 │ │
│ │         """Generate multiple abstract pairs for randomization."""        │ │
│ │         pairs = []                                                       │ │
│ │         for _ in range(n_pairs):                                         │ │
│ │             pair = self.generate_abstract_pair()                         │ │
│ │             pairs.append(pair)                                           │ │
│ │         return pairs                                                     │ │
│ │                                                                          │ │
│ │     def save_abstract_pool(self, n_pairs: int = 50, filename: str =      │ │
│ │ 'abstract_pool.json'):                                                   │ │
│ │         """Generate and save large pool of abstracts for study."""       │ │
│ │         pairs = self.generate_multiple_pairs(n_pairs)                    │ │
│ │                                                                          │ │
│ │         # Format for OSF/supplementary material                          │ │
│ │         abstract_pool = {                                                │ │
│ │             'metadata': {                                                │ │
│ │                 'total_pairs': n_pairs,                                  │ │
│ │                 'generation_method': 'systematic_template_based',        │ │
│ │                 'topics_covered': [template.topic for template in        │ │
│ │ self.abstract_templates],                                                │ │
│ │                 'causal_categories': list(self.causal_terms.keys()),     │ │
│ │                 'quality_control': 'manual_review_required'              │ │
│ │             },                                                           │ │
│ │             'abstracts': []                                              │ │
│ │         }                                                                │ │
│ │                                                                          │ │
│ │         for i, (high, low) in enumerate(pairs):                          │ │
│ │             abstract_pool['abstracts'].append({                          │ │
│ │                 'pair_id': i + 1,                                        │ │
│ │                 'high_density': high,                                    │ │
│ │                 'low_density': low,                                      │ │
│ │                 'topic_match': high['topic'] == low['topic']             │ │
│ │             })                                                           │ │
│ │                                                                          │ │
│ │         with open(filename, 'w') as f:                                   │ │
│ │             json.dump(abstract_pool, f, indent=2)                        │ │
│ │                                                                          │ │
│ │         print(f"Generated {n_pairs} abstract pairs saved to {filename}") │ │
│ │         print(f"Topics covered: {len(self.abstract_templates)}")         │ │
│ │         return abstract_pool                                             │ │
│ │                                                                          │ │
│ │ def main():                                                              │ │
│ │     generator = AbstractGenerator()                                      │ │
│ │                                                                          │ │
│ │     # Generate sample pair                                               │ │
│ │     high, low = generator.generate_abstract_pair()                       │ │
│ │     print("Sample High Density Abstract:")                               │ │
│ │     print(f"Topic: {high['topic']}")                                     │ │
│ │     print(f"Density: {high['density']:.2f}")                             │ │
│ │     print(f"Text: {high['text']}")                                       │ │
│ │     print()                                                              │ │
│ │     print("Sample Low Density Abstract:")                                │ │
│ │     print(f"Topic: {low['topic']}")                                      │ │
│ │     print(f"Density: {low['density']:.2f}")                              │ │
│ │     print(f"Text: {low['text']}")                                        │ │
│ │                                                                          │ │
│ │     # Generate pool for study                                            │ │
│ │     pool = generator.save_abstract_pool(50)                              │ │
│ │                                                                          │ │
│ │ if __name__ == "__main__":                                               │ │
│ │     main()            





