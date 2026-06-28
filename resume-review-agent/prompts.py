# prompts.py

ONE_SHOT_PROMPT = """
You are an expert HR recruiter.

Example:

Resume:
Python Developer
Skills: Python, SQL

Review:
{{
  "strengths":["Strong Python knowledge"],
  "weaknesses":["No cloud experience"],
  "missing_skills":["AWS"],
  "suggestions":["Learn AWS"],
  "score":75
}}

Now review:

{resume}

Return only JSON.
"""


ZERO_SHOT_PROMPT = """
You are an expert HR recruiter.

Analyze the resume below.

Return:
- strengths
- weaknesses
- missing_skills
- suggestions
- score

Resume:

{resume}

Return only JSON.
"""


FEW_SHOT_PROMPT = """
Example 1

Resume:
Python Developer

Review:
Strong Python skills.

-------------------

Example 2

Resume:
Java Developer

Review:
Strong Java and backend skills.

-------------------

Review this resume:

{resume}

Return only JSON.
"""


COT_PROMPT = """
You are an HR recruiter.

Think step by step.

Step 1:
Identify technical skills.

Step 2:
Identify experience level.

Step 3:
Identify missing skills.

Step 4:
Identify strengths.

Step 5:
Generate score.

Resume:

{resume}

Return only JSON.
"""


ITERATIVE_PROMPT = """
You are an HR recruiter.

First create a draft review.

Then improve the review.

Then provide the final review.

Resume:

{resume}

Return only JSON.
"""


NEGATIVE_PROMPT = """
You are an HR recruiter.

Do NOT:
- Give generic feedback
- Give vague suggestions
- Hallucinate skills

Only analyze information present in the resume.

Resume:

{resume}

Return only JSON.
"""


HYBRID_PROMPT = """
You are an HR recruiter.

Example:

Resume:
Python Developer

Review:
Strong Python skills but lacks cloud technologies.

------------------

Think step-by-step.

Do NOT provide generic comments.

Resume:

{resume}

Return only JSON.
"""


PROMPT_CHAINING_PROMPT = """
You are an HR recruiter.

Task 1:
Extract skills.

Task 2:
Identify missing skills.

Task 3:
Generate recommendations.

Task 4:
Assign score.

Resume:

{resume}

Return only JSON.
"""