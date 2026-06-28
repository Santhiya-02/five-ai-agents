import os
from groq import Groq
from dotenv import load_dotenv
from prompts import (
    ZERO_SHOT_PROMPT, ONE_SHOT_PROMPT, FEW_SHOT_PROMPT, COT_PROMPT,
    ITERATIVE_PROMPT, NEGATIVE_PROMPT, HYBRID_PROMPT, PROMPT_CHAINING_PROMPT,
)

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
SYSTEM_PROMPT = """
You are a Resume Review Assistant.
Analyze resumes and evaluate:
- Skills
- Projects
- Experience
- Education
- Strengths
- Weaknesses
- Missing Information
- Overall Suitability
Provide constructive improvement suggestions to increase employability.
Rules:
- Accept only resumes, CVs, professional profiles, or candidate information.
- Extract and assess technical skills, soft skills, projects, certifications, education, and work experience.
- Evaluate project quality, skill relevance, and resume completeness.
- Identify missing sections or weak areas.
- Do not answer general questions.
- Do not provide coding assistance.
- Do not explain technical concepts.
- Do not provide career advice unrelated to resume review.
- Return only valid JSON.
- Do not include markdown, explanations, or additional text.
If the input is not a resume, CV, professional profile, or candidate information, return exactly:
{
  "error": "Invalid input. A resume is required."
}"""
resume = """
Java Developer

Skills:
Java
Spring Boot
MySQL

Projects:
E-Commerce Website
"""
prompts = {
    "one_shot": ONE_SHOT_PROMPT
}

for name, template in prompts.items():

    print("\n" + "=" * 60)
    print(f"TECHNIQUE: {name.upper()}")
    print("=" * 60)

    prompt = template.format(resume=resume)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
             {
            "role": "system",
            "content": SYSTEM_PROMPT
        },{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=600,
        response_format={"type": "json_object"},
        seed=43
    )
    
    print(response.choices[0].message.content)