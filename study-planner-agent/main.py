
import os
from groq import Groq
from dotenv import load_dotenv
from prompts import (
    ONE_SHOT_PROMPT,
    ZERO_SHOT_PROMPT,
    FEW_SHOT_PROMPT,
    COT_PROMPT,
    ITERATIVE_PROMPT,
    NEGATIVE_PROMPT,
    HYBRID_PROMPT,
    PROMPT_CHAINING_PROMPT,
)

load_dotenv(
    dotenv_path=os.path.join(
        os.path.dirname(__file__),
        "..",
        ".env"
    )
)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
SYSTEM_PROMPT = """
You are a Study Planner Agent.
Your task is to create personalized study plans based on the user's goals, subjects, available time, deadlines, and current skill level.
Responsibilities:
- Analyze study requirements and goals.
- Create structured study schedules.
- Break large goals into manageable tasks.
- Prioritize important topics.
- Recommend revision and practice sessions.
- Adjust plans based on available time and deadlines.
Rules:
- Focus only on study planning and learning schedules.
- Provide realistic and achievable plans.
- Consider workload, exam dates, and learning pace.
- Encourage consistency and regular revision.
- Do not answer unrelated questions.
- Do not provide career counseling unrelated to study planning.
- Do not provide medical, legal, or financial advice.
For every valid request, return:
Goal: <study objective>
Duration: <timeline>
Daily Study Time: <hours/day>
Study Plan
Priority Topics
Revision Strategy
Recommendations
If the input is not related to study planning, exams, learning goals, or academic preparation, respond with:
"Out of Scope: Please provide a study goal, subject, exam, or learning objective."
```
"""

student = """
Subject: Machine Learning
Exam in: 7 days
Daily available hours: 3
Current level: Beginner
Topics to cover: Linear Regression, Logistic Regression, Decision Trees, SVM, K-Means, Neural Networks, Model Evaluation
"""

PROMPTS = {
    "cot": COT_PROMPT,
}

results = {}

for technique, prompt in PROMPTS.items():

    try:
        final_prompt = prompt.format(student=student)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                    {
            "role": "system",
            "content": SYSTEM_PROMPT
            },
                {
                    "role": "user",
                    "content": final_prompt
                }
            ],
            temperature=0.2,
            top_p=1.0,
            max_tokens=1000,
            seed=47,
            response_format={"type": "json_object"},
        )

        results[technique] = response.choices[0].message.content

    except Exception as e:
        results[technique] = f"ERROR: {e}"

for technique, output in results.items():

    print("\n" + "=" * 60)
    print(f"TECHNIQUE: {technique.upper()}")
    print("=" * 60)
    print(output)
