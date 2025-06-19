 import json
    import random
    from typing import Dict, List, Tuple
    from pathlib import Path

    class SurveyGenerator:
        def __init__(self):
            self.high_density_abstracts = [
                {
                    "id": "hd1",
                    "text": """This article sustains that neural plasticity
     subyace higher cognitive processes, 
                    enabling complex interactions that play a crucial role 
    in memory formation. The underlying 
                    mechanisms presuppose bidirectional feedback loops that
     translate into observable behavioral 
                    outcomes. Statistical analysis reveals significant 
    predictors and explains variance through 
                    mediating variables that function as catalysts in the 
    cognitive framework.""",
                    "density": 8.5
                },
                {
                    "id": "hd2",
                    "text": """The research demonstrates that social 
    isolation inhibits psychological well-being while 
                    simultaneously facilitating maladaptive coping 
    strategies. These reciprocal processes 
                    sustain a dialectical relationship where loneliness 
    serves as both predictor and outcome. 
                    The cornerstone of this framework lies in understanding
     how environmental factors 
                    moderate the indirect effects of social connectedness 
    on mental health outcomes.""",
                    "density": 9.2
                },
                {
                    "id": "hd3",
                    "text": """This investigation reveals how technological
     determinism underlies contemporary ethical 
                    debates, functioning as the foundation for moral 
    reasoning in digital contexts. The 
                    analysis sustains that algorithmic bias translates into
     systemic discrimination through 
                    mediating pathways that inhibit equitable outcomes. 
    These mechanisms presuppose 
                    reciprocal interactions between human agency and 
    machine learning processes.""",
                    "density": 8.8
                }
            ]

            self.low_density_abstracts = [
                {
                    "id": "ld1",
                    "text": """This article examines the relationship 
    between neural plasticity and higher cognitive 
                    processes in memory formation. The study investigates 
    how different mechanisms contribute 
                    to behavioral outcomes. Statistical analysis shows 
    important factors and describes 
                    patterns in the cognitive framework through various 
    measured variables.""",
                    "density": 2.1
                },
                {
                    "id": "ld2",
                    "text": """The research explores how social isolation 
    affects psychological well-being and coping 
                    strategies. These processes show connections where 
    loneliness appears as both a factor 
                    and result. The study focuses on understanding how 
    environmental conditions influence 
                    the relationship between social connection and mental 
    health.""",
                    "density": 1.8
                },
                {
                    "id": "ld3",
                    "text": """This investigation examines technological 
    determinism in contemporary ethical debates, 
                    as a basis for moral reasoning in digital contexts. The
     analysis shows that algorithmic 
                    bias creates systemic discrimination through pathways 
    that affect equitable outcomes. 
                    These processes involve interactions between human 
    agency and machine learning.""",
                    "density": 2.3
                }
            ]

        def generate_survey_questions(self) -> List[Dict]:
            """Generate structured survey questions for causal language 
    assessment."""
            questions = []

            # Demographic questions
            questions.append({
                "id": "demo_age",
                "type": "number",
                "question": "What is your age?",
                "required": True,
                "min_value": 18,
                "max_value": 100
            })

            questions.append({
                "id": "demo_education",
                "type": "select",
                "question": "What is your highest level of education?",
                "options": [
                    "High school or equivalent",
                    "Some college",
                    "Bachelor's degree",
                    "Master's degree",
                    "Doctoral degree",
                    "Other"
                ],
                "required": True
            })

            questions.append({
                "id": "demo_philosophy_familiarity",
                "type": "likert",
                "question": "How familiar are you with philosophical 
    academic writing?",
                "scale": 5,
                "labels": ["Not at all familiar", "Slightly familiar",
    "Moderately familiar",
                          "Very familiar", "Extremely familiar"],
                "required": True
            })

            # Abstract comparison questions
            abstract_pairs = self._create_abstract_pairs()

            for i, (high_density, low_density) in
    enumerate(abstract_pairs):
                questions.extend([
                    {
                        "id": f"abstract_pair_{i+1}_presentation",
                        "type": "display",
                        "content": {
                            "abstract_a": {
                                "title": f"Abstract A",
                                "text": high_density["text"]
                            },
                            "abstract_b": {
                                "title": f"Abstract B",
                                "text": low_density["text"]
                            }
                        }
                    },
                    {
                        "id": f"abstract_pair_{i+1}_clarity",
                        "type": "select",
                        "question": "Which abstract is clearer and easier 
    to understand?",
                        "options": ["Abstract A", "Abstract B", "Both are 
    equally clear", "Neither is clear"],
                        "required": True
                    },
                    {
                        "id": f"abstract_pair_{i+1}_clarity_rating_a",
                        "type": "likert",
                        "question": "Rate the clarity of Abstract A:",
                        "scale": 5,
                        "labels": ["Very unclear", "Unclear", "Neutral",
    "Clear", "Very clear"],
                        "required": True
                    },
                    {
                        "id": f"abstract_pair_{i+1}_clarity_rating_b",
                        "type": "likert",
                        "question": "Rate the clarity of Abstract B:",
                        "scale": 5,
                        "labels": ["Very unclear", "Unclear", "Neutral",
    "Clear", "Very clear"],
                        "required": True
                    },
                    {
                        "id": f"abstract_pair_{i+1}_cognitive_load_a",
                        "type": "likert",
                        "question": "How much mental effort did Abstract A 
    require to understand?",
                        "scale": 5,
                        "labels": ["Very little effort", "Little effort",
    "Moderate effort",
                                  "Much effort", "Very much effort"],
                        "required": True
                    },
                    {
                        "id": f"abstract_pair_{i+1}_cognitive_load_b",
                        "type": "likert",
                        "question": "How much mental effort did Abstract B 
    require to understand?",
                        "scale": 5,
                        "labels": ["Very little effort", "Little effort",
    "Moderate effort",
                                  "Much effort", "Very much effort"],
                        "required": True
                    },
                    {
                        "id": f"abstract_pair_{i+1}_causal_language_a",
                        "type": "likert",
                        "question": "Rate the use of causal language (words
     indicating cause-effect relationships) in Abstract A:",
                        "scale": 5,
                        "labels": ["Too little", "Too few", "Just right",
    "Too many", "Far too many"],
                        "required": True
                    },
                    {
                        "id": f"abstract_pair_{i+1}_causal_language_b",
                        "type": "likert",
                        "question": "Rate the use of causal language (words
     indicating cause-effect relationships) in Abstract B:",
                        "scale": 5,
                        "labels": ["Too little", "Too few", "Just right",
    "Too many", "Far too many"],
                        "required": True
                    }
                ])

            # General assessment questions
            questions.extend([
                {
                    "id": "general_causal_preference",
                    "type": "likert",
                    "question": "In general, do you prefer academic 
    abstracts that use more explicit causal language?",
                    "scale": 5,
                    "labels": ["Strongly disagree", "Disagree", "Neutral",
    "Agree", "Strongly agree"],
                    "required": True
                },
                {
                    "id": "general_comprehension_impact",
                    "type": "likert",
                    "question": "Do you think explicit causal language 
    improves comprehension of philosophical texts?",
                    "scale": 5,
                    "labels": ["Strongly disagree", "Disagree", "Neutral",
    "Agree", "Strongly agree"],
                    "required": True
                },
                {
                    "id": "open_feedback",
                    "type": "textarea",
                    "question": "Please provide any additional comments 
    about causal language in philosophical writing:",
                    "required": False,
                    "placeholder": "Your thoughts on the use of causal 
    language in academic philosophy..."
                }
            ])

            return questions

        def _create_abstract_pairs(self) -> List[Tuple[Dict, Dict]]:
            """Create randomized pairs of high and low density 
    abstracts."""
            pairs = []

            # Ensure we have pairs
            min_pairs = min(len(self.high_density_abstracts),
    len(self.low_density_abstracts))

            high_shuffled = random.sample(self.high_density_abstracts,
    min_pairs)
            low_shuffled = random.sample(self.low_density_abstracts,
    min_pairs)

            for high, low in zip(high_shuffled, low_shuffled):
                pairs.append((high, low))

            return pairs

        def generate_html_survey(self, questions: List[Dict]) -> str:
            """Generate HTML survey for GitHub Pages deployment."""
            html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, 
    initial-scale=1.0">
        <title>Causal Language in Philosophy Survey</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, 
    sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                line-height: 1.6;
                background-color: #f5f5f5;
            }
            .survey-container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            .question-block {
                margin-bottom: 25px;
                padding: 20px;
                border-left: 4px solid #007bff;
                background-color: #f8f9fa;
            }
            .abstract-display {
                display: flex;
                gap: 20px;
                margin: 20px 0;
            }
            .abstract-box {
                flex: 1;
                padding: 15px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: white;
            }
            .abstract-title {
                font-weight: bold;
                margin-bottom: 10px;
                color: #007bff;
            }
            .likert-scale {
                display: flex;
                justify-content: space-between;
                margin: 10px 0;
            }
            .likert-option {
                display: flex;
                flex-direction: column;
                align-items: center;
                flex: 1;
                margin: 0 5px;
            }
            .likert-option input[type="radio"] {
                margin-bottom: 5px;
            }
            .likert-option label {
                font-size: 0.9em;
                text-align: center;
            }
            .question-title {
                font-weight: bold;
                margin-bottom: 10px;
                color: #333;
            }
            .submit-btn {
                background-color: #007bff;
                color: white;
                padding: 12px 30px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                margin-top: 20px;
            }
            .submit-btn:hover {
                background-color: #0056b3;
            }
            .progress-bar {
                width: 100%;
                height: 10px;
                background-color: #e0e0e0;
                border-radius: 5px;
                margin-bottom: 20px;
            }
            .progress-fill {
                height: 100%;
                background-color: #007bff;
                border-radius: 5px;
                transition: width 0.3s ease;
            }
        </style>
    </head>
    <body>
        <div class="survey-container">
            <h1>Causal Language in Philosophical Writing Survey</h1>
            <p>This survey examines how causal language affects the clarity
     and comprehension of philosophical abstracts. 
            Your participation will contribute to research on improving 
    academic communication in philosophy.</p>
            
            <div class="progress-bar">
                <div class="progress-fill" id="progressFill" style="width: 
    0%"></div>
            </div>
            
            <form id="surveyForm">
                {questions_html}
                
                <button type="submit" class="submit-btn">Submit 
    Survey</button>
            </form>
        </div>
        
        <script>
            {javascript_code}
        </script>
    </body>
    </html>
            """

            questions_html = self._generate_questions_html(questions)
            javascript_code = self._generate_javascript_code(questions)

            return html_template.replace("{questions_html}",
    questions_html).replace("{javascript_code}", javascript_code)

        def _generate_questions_html(self, questions: List[Dict]) -> str:
            """Generate HTML for survey questions."""
            html_parts = []

            for i, question in enumerate(questions):
                if question["type"] == "display":

    html_parts.append(self._create_abstract_display_html(question, i))
                elif question["type"] == "likert":
                    html_parts.append(self._create_likert_html(question,
    i))
                elif question["type"] == "select":
                    html_parts.append(self._create_select_html(question,
    i))
                elif question["type"] == "number":
                    html_parts.append(self._create_number_html(question,
    i))
                elif question["type"] == "textarea":
                    html_parts.append(self._create_textarea_html(question,
    i))

            return "\n".join(html_parts)

        def _create_abstract_display_html(self, question: Dict, index: int)
     -> str:
            """Create HTML for abstract display."""
            content = question["content"]
            return f"""
            <div class="question-block" data-question="{index}">
                <div class="abstract-display">
                    <div class="abstract-box">
                        <div 
    class="abstract-title">{content['abstract_a']['title']}</div>
                        <div>{content['abstract_a']['text']}</div>
                    </div>
                    <div class="abstract-box">
                        <div 
    class="abstract-title">{content['abstract_b']['title']}</div>
                        <div>{content['abstract_b']['text']}</div>
                    </div>
                </div>
            </div>
            """

        def _create_likert_html(self, question: Dict, index: int) -> str:
            """Create HTML for Likert scale questions."""
            scale_html = []
            for i in range(question["scale"]):
                label = question["labels"][i] if i <
    len(question["labels"]) else str(i+1)
                scale_html.append(f"""
                    <div class="likert-option">
                        <input type="radio" id="{question['id']}_{i+1}" 
    name="{question['id']}" value="{i+1}" {'required' if 
    question.get('required') else ''}>
                        <label for="{question['id']}_{i+1}">{label}</label>
                    </div>
                """)

            return f"""
            <div class="question-block" data-question="{index}">
                <div class="question-title">{question['question']}</div>
                <div class="likert-scale">
                    {''.join(scale_html)}
                </div>
            </div>
            """

        def _create_select_html(self, question: Dict, index: int) -> str:
            """Create HTML for select questions."""
            options_html = []
            for option in question["options"]:
                options_html.append(f'<option 
    value="{option}">{option}</option>')

            return f"""
            <div class="question-block" data-question="{index}">
                <div class="question-title">{question['question']}</div>
                <select name="{question['id']}" {'required' if 
    question.get('required') else ''}>
                    <option value="">Please select...</option>
                    {''.join(options_html)}
                </select>
            </div>
            """

        def _create_number_html(self, question: Dict, index: int) -> str:
            """Create HTML for number input questions."""
            return f"""
            <div class="question-block" data-question="{index}">
                <div class="question-title">{question['question']}</div>
                <input type="number" name="{question['id']}" 
                       min="{question.get('min_value', '')}" 
                       max="{question.get('max_value', '')}"
                       {'required' if question.get('required') else ''}>
            </div>
            """

        def _create_textarea_html(self, question: Dict, index: int) -> str:
            """Create HTML for textarea questions."""
            return f"""
            <div class="question-block" data-question="{index}">
                <div class="question-title">{question['question']}</div>
                <textarea name="{question['id']}" rows="4" cols="50" 
                          placeholder="{question.get('placeholder', '')}"
                          {'required' if question.get('required') else 
    ''}></textarea>
            </div>
            """

        def _generate_javascript_code(self, questions: List[Dict]) -> str:
            """Generate JavaScript for survey functionality."""
            return """
            document.addEventListener('DOMContentLoaded', function() {
                const form = document.getElementById('surveyForm');
                const progressFill = 
    document.getElementById('progressFill');
                const questionBlocks = 
    document.querySelectorAll('.question-block');
                
                // Update progress bar
                function updateProgress() {
                    const inputs = form.querySelectorAll('input, select, 
    textarea');
                    const filled = Array.from(inputs).filter(input => {
                        if (input.type === 'radio') {
                            return 
    form.querySelector(`input[name="${input.name}"]:checked`);
                        }
                        return input.value.trim() !== '';
                    });
                    
                    const progress = (filled.length / inputs.length) * 100;
                    progressFill.style.width = progress + '%';
                }
                
                // Add event listeners
                form.addEventListener('change', updateProgress);
                form.addEventListener('input', updateProgress);
                
                // Form submission
                form.addEventListener('submit', function(e) {
                    e.preventDefault();
                    
                    const formData = new FormData(form);
                    const data = {};
                    
                    for (let [key, value] of formData.entries()) {
                        data[key] = value;
                    }
                    
                    // Add timestamp and session info
                    data.timestamp = new Date().toISOString();
                    data.session_id = 'session_' + 
    Math.random().toString(36).substr(2, 9);
                    
                    // In a real deployment, this would send to your data 
    collection endpoint
                    console.log('Survey Data:', data);
                    alert('Survey completed! Thank you for your 
    participation.');
                    
                    // For Prolific integration, you would redirect to 
    completion URL here
                    // window.location.href = 
    'https://app.prolific.co/submissions/complete?cc=COMPLETION_CODE';
                });
                
                // Initialize progress
                updateProgress();
            });
            """

        def save_survey_files(self, output_dir: str = '../survey/'):
            """Generate and save survey files for deployment."""
            Path(output_dir).mkdir(exist_ok=True)

            # Generate questions
            questions = self.generate_survey_questions()

            # Save questions JSON for analysis
            with open(f'{output_dir}survey_questions.json', 'w') as f:
                json.dump(questions, f, indent=2)

            # Generate and save HTML survey
            html_survey = self.generate_html_survey(questions)
            with open(f'{output_dir}index.html', 'w') as f:
                f.write(html_survey)

            # Create deployment instructions
            deployment_instructions = """
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
    """

            with open(f'{output_dir}deployment_instructions.md', 'w') as f:
                f.write(deployment_instructions)

            print(f"Survey files generated in {output_dir}")
            print("Files created:")
            print("- index.html (main survey)")
            print("- survey_questions.json (question structure)")
            print("- deployment_instructions.md (setup guide)")

    def main():
        generator = SurveyGenerator()
        generator.save_survey_files()

    if __name__ == "__main__":
        main()





