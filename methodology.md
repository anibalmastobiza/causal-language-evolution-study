## Research Design Overview

    This computational study employs a mixed-methods approach combining:
    1. **Corpus Analysis**: Automated detection and temporal analysis of
    causal terms
    2. **Experimental Validation**: Survey-based assessment of causal
    language clarity
    3. **Statistical Analysis**: Comprehensive trend analysis and
    hypothesis testing

    ## Corpus Collection (1950-2025)

    ### Data Sources
    - **Primary**: CrossRef API for open access philosophical papers
    - **Secondary**: PhilPapers database (institutional access required)
    - **Tertiary**: JSTOR and Web of Science (subject to licensing)

    ### Selection Criteria
    - **Language**: English abstracts only
    - **Discipline**: Philosophy and related subdisciplines
    - **Time Range**: 1950-2025 (75-year span)
    - **Quality**: Peer-reviewed journal articles
    - **Length**: Abstracts between 100-2000 characters

    ### Subdiscipline Classification
    - Ethics and Moral Philosophy
    - Epistemology
    - Philosophy of Science
    - Metaphysics
    - Philosophy of Mind
    - Political Philosophy
    - Logic and Philosophy of Language

    ## Causal Term Detection System

    ### Advanced Typology of Causal Language

    #### 1. Enablement/Foundation Terms
    - **Spanish**: posibilitar, subyacer, sustentar, presuponer
    - **English**: enable, underlie, sustain, presuppose, facilitate,
    ground
    - **Function**: Express foundational or enabling causal relationships

    #### 2. Inhibition/Prevention Terms
    - **Spanish**: impedir, inhibir, limitar, obstaculizar, atenuar
    - **English**: prevent, inhibit, limit, obstruct, hinder, constrain
    - **Function**: Express blocking or limiting causal relationships

    #### 3. Reciprocal Causal Terms
    - **Spanish**: retroalimentarse, interactuar, relación dialéctica
    - **English**: feedback, interact, reciprocal, bidirectional, circular
    causation
    - **Function**: Express mutual or bidirectional causal relationships

    #### 4. Phraseological Expressions
    - **Spanish**: piedra angular, sentar bases, catalizador, traducirse en
    - **English**: cornerstone, lay foundation, catalyst, translate into,
    play role
    - **Function**: Metaphorical expressions of causal relationships

    #### 5. Statistical/Methodological Terms
    - **English**: predict, explain variance, significant predictor,
    correlation, regression
    - **Function**: Express empirical/statistical causal relationships

    #### 6. Mediation/Moderation Terms
    - **English**: mediation, moderation, indirect effect, pathway,
    mechanism
    - **Function**: Express complex, multi-step causal relationships

    ### Detection Algorithm
    1. **Preprocessing**: Text normalization, tokenization
    2. **Pattern Matching**: Regex-based detection with morphological
    variants
    3. **Context Validation**: Semantic filtering to reduce false positives
    4. **Density Calculation**: Terms per 100 words normalization

    ## Temporal Analysis Framework

    ### Temporal Segmentation
    - **Decades**: 1950s, 1960s, 1970s, 1980s, 1990s, 2000s, 2010s, 2020s
    - **Analysis Unit**: Individual abstracts with year metadata
    - **Trend Detection**: Linear regression, correlation analysis

    ### Statistical Methods
    - **Descriptive Statistics**: Mean, median, standard deviation by
    period
    - **Trend Analysis**: Pearson correlation, linear regression slopes
    - **Significance Testing**: p-values for temporal correlations
    - **Effect Sizes**: Cohen's d for magnitude assessment

    ## Experimental Survey Design

    ### Stimulus Materials
    - **High Density Abstracts**: >7 causal terms per 100 words
    - **Low Density Abstracts**: <3 causal terms per 100 words
    - **Content Matching**: Same philosophical topics, different causal
    language density

    ### Participant Recruitment
    - **Platform**: Prolific Academic
    - **Sample Size**: n > 300 (power analysis: d=0.5, α=0.05, β=0.20)
    - **Inclusion Criteria**:
      - Age 18+
      - Native English speakers
      - 95%+ approval rate on Prolific

    ### Measures

    #### Primary Dependent Variables
    1. **Clarity Rating**: 5-point Likert scale (1=Very unclear, 5=Very
    clear)
    2. **Cognitive Load**: 5-point Likert scale (1=Very little effort,
    5=Very much effort)
    3. **Preference**: Binary choice between abstract versions

    #### Secondary Variables
    1. **Causal Language Assessment**: Rating of causal term usage
    appropriateness
    2. **Comprehension**: Open-ended understanding assessment
    3. **Demographics**: Age, education, philosophy familiarity

    ### Experimental Procedure
    1. **Consent and Demographics** (2 minutes)
    2. **Instructions and Practice** (3 minutes)
    3. **Abstract Comparisons** (15 minutes)
       - 3 paired comparisons
       - Randomized presentation order
       - Within-subjects design
    4. **General Assessment Questions** (5 minutes)
    5. **Debriefing** (2 minutes)

    **Total Duration**: ~25 minutes

    ## Statistical Analysis Plan

    ### Descriptive Analysis
    - Temporal trends in causal term usage
    - Subdiscipline comparisons
    - Category-specific evolution patterns

    ### Inferential Statistics

    #### Corpus Analysis
    1. **Temporal Trends**:
       - Linear regression: Year → Causal Density
       - Correlation analysis for each category
       - ANOVA: Decade × Causal Density

    2. **Subdiscipline Comparison**:
       - One-way ANOVA: Subdiscipline × Causal Density
       - Post-hoc Tukey HSD tests
       - Effect size calculations (η²)

    #### Survey Analysis
    1. **Primary Hypotheses**:
       - H1: Low density abstracts rated higher for clarity
       - H2: High density abstracts require more cognitive effort
       - H3: Participants prefer moderate causal language density

    2. **Statistical Tests**:
       - Paired t-tests for within-subjects comparisons
       - Repeated measures ANOVA
       - Effect sizes (Cohen's d)

    ### Power Analysis
    - **Corpus Analysis**: n=1000+ abstracts for trend detection
    - **Survey**: n=300+ for medium effect size detection (d=0.5)
    - **Alpha Level**: 0.05
    - **Power**: 0.80

    ## Ethical Considerations

    ### Data Privacy
    - Anonymized corpus data only
    - Survey responses anonymized post-collection
    - No personal identifiers retained

    ### Informed Consent
    - Clear explanation of study purpose
    - Voluntary participation
    - Right to withdraw
    - Compensation via Prolific standard rates

    ### Open Science Practices
    - Pre-registration of hypotheses
    - Open data sharing (anonymized)
    - Reproducible analysis code
    - FAIR data principles compliance

    ## Validation and Reliability

    ### Corpus Validation
    - **Inter-rater Reliability**: Manual coding subset (κ > 0.80)
    - **Algorithm Validation**: Precision/recall on gold standard
    - **Content Validity**: Philosophy expert review

    ### Survey Validation
    - **Pilot Testing**: n=50 preliminary validation
    - **Internal Consistency**: Cronbach's α for multi-item scales
    - **Test-retest Reliability**: Subset retesting (r > 0.70)

    ## Expected Outcomes and Impact

    ### Primary Research Questions
    1. How has causal language usage evolved in philosophical abstracts
    (1950-2025)?
    2. Which categories of causal terms show significant temporal trends?
    3. Do subdisciplines differ in causal language density and evolution?
    4. Does causal language density affect comprehension and cognitive
    load?

    ### Anticipated Contributions
    - **Theoretical**: Understanding of philosophical discourse evolution
    - **Methodological**: Computational approach to discourse analysis
    - **Practical**: Guidelines for clearer philosophical communication
    - **Interdisciplinary**: Bridge between philosophy, linguistics, and
    cognitive science

    ### Publication Strategy
    - **Target Journals**:
      - Primary: Journal of Digital Humanities, Digital Scholarship in the
    Humanities
      - Secondary: Philosophical Studies, Metaphilosophy
      - Complementary: AI & Society, Language Resources and Evaluation

    ### Limitations and Future Directions
    - **Language Bias**: English-only corpus
    - **Access Limitations**: Potential database restrictions
    - **Temporal Coverage**: Uneven historical representation
    - **Future Work**: Multilingual expansion, full-text analysis,
    author-level studies



⏺ 10. survey/deployment_instructions.md (COMPLETO)

⏺ Read(file_path: "/Users/anibalmonasterioastobiza/causal-language-evolutio
      n-study/survey/deployment_instructions.md")
  ⎿                                                                        
     # Survey Deployment Instructions

     ## GitHub Pages Deployment
     1. Create a new GitHub repository
     2. Upload survey files to the repository
     3. Enable GitHub Pages in repository settings
     4. Use the GitHub Pages URL for Prolific

     ## Prolific Integration
     1. Set completion URL:
     https://app.prolific.co/submissions/complete?cc=YOUR_COMPLETION_CODE
     2. Set survey URL: https://yourusername.github.io/repository-name/
     3. Configure participant requirements:
        - Age: 18+
        - Language: English (native)
        - Approval rate: 95%+

     ## Data Collection
     - Survey responses logged to browser console (development)
     - For production, implement server endpoint for data storage
     - Consider using services like Formspree, Google Forms API, or custom
     backend

     ## Sample Size Calculation
     - Target n > 300 participants as specified
     - Power analysis for medium effect size (d = 0.5)
     - Alpha = 0.05, Power = 0.80


