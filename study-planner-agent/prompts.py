ZERO_SHOT_PROMPT = """
Create a study plan for the student below.

Return:

* subject
* total_days
* daily_hours
* topics (list)
* schedule (day-by-day plan)
* tips (list)

Student Info:

{student}

Return only JSON.
"""

ONE_SHOT_PROMPT = """
You are an expert study planner.

Example:

Student:
Subject: Python
Exam in: 5 days
Daily available hours: 2

Plan:
{{
"subject": "Python",
"total_days": 5,
"daily_hours": 2,
"topics": ["Basics", "Functions", "OOP", "File I/O", "Practice Tests"],
"schedule": {{
"Day 1": "Basics",
"Day 2": "Functions",
"Day 3": "OOP",
"Day 4": "File I/O",
"Day 5": "Practice Tests"
}},
"tips": ["Code daily", "Use flashcards", "Review weak topics"]
}}

Now create a plan for:

{student}
"""

FEW_SHOT_PROMPT = """
Example 1

Student:
Subject: Math
Exam in: 3 days
Daily available hours: 3

Plan:
{{"subject":"Math","total_days":3,
"daily_hours":3,
"topics":["Algebra","Geometry","Practice"],
"schedule":{{"Day 1":"Algebra","Day 2":"Geometry",
"Day 3":"Practice"}},
"tips":["Solve past papers","Focus on weak areas"]}}

---

Example 2

Student:
Subject: History
Exam in: 7 days
Daily available hours: 1

Plan:
{{"subject":"History","total_days":7,
"daily_hours":1,
"topics":["Ancient","Medieval","Modern","WWI","WWII","Cold War","Revision"],
"schedule":{{"Day 1":"Ancient","Day 2":"Medieval","Day 3":"Modern",
"Day 4":"WWI","Day 5":"WWII","Day 6":"Cold War","Day 7":"Revision"}},
"tips":["Use timelines","Make notes","Summarize chapters"]}}

---

Example 3

Student:
Subject: Biology
Exam in: 4 days
Daily available hours: 2

Plan:
{{"subject":"Biology","total_days":4,
"daily_hours":2,
"topics":["Cell Biology","Genetics","Ecology","Revision"],
"schedule":{{"Day 1":"Cell Biology","Day 2":"Genetics",
"Day 3":"Ecology","Day 4":"Revision"}},
"tips":["Draw diagrams","Use mnemonics","Review past papers"]}}

---

Now create a plan for:

{student}

Return only JSON.
"""

COT_PROMPT = """
You are a study planner.

Think step by step.

Step 1: Identify the subject and total available days.
Step 2: Break the subject into key topics.
Step 3: Distribute topics across days based on available hours.
Step 4: Assign one or more topics per day.
Step 5: Generate practical study tips for this subject.

Student Info:

{student}

Return only JSON.
"""

ITERATIVE_PROMPT = """
You are a study planner.

First pass: Draft an initial study plan based on the student info.
Second pass: Review and balance the workload across days.
Final pass: Output the refined and final study plan.

Student Info:

{student}

Return only JSON.
"""

NEGATIVE_PROMPT = """
You are a study planner.

Do NOT:

* Overload a single day with too many topics
* Recommend more hours than the student has available
* Give generic or vague tips
* Hallucinate subjects or topics not related to the student's subject

Only use information provided in the student info.

Student Info:

{student}

Return only JSON.
"""

HYBRID_PROMPT = """
You are a study planner.

Example:

Student:
Subject: JavaScript
Exam in: 4 days
Daily available hours: 3

Plan:
{{"subject":"JavaScript",
"total_days":4,
"daily_hours":3,
"topics":["Syntax & Variables","Functions & Arrays","DOM Manipulation","Practice & Revision"],
"schedule":{{"Day 1":"Syntax & Variables",
"Day 2":"Functions & Arrays",
"Day 3":"DOM Manipulation",
"Day 4":"Practice & Revision"}},
"tips":["Build small projects","Use browser console","Review MDN docs"]}}

---

Think step-by-step. Do NOT overload any single day. Balance the plan evenly.

Student Info:

{student}

Return only JSON.
"""

PROMPT_CHAINING_PROMPT = """
You are a study planner.

Task 1: Extract subject, exam days, and daily available hours.
Task 2: Break the subject into logical topics ordered by difficulty.
Task 3: Distribute topics evenly across the available days.
Task 4: Generate specific, actionable study tips for the subject.
Task 5: Compile everything into the final study plan.

Student Info:

{student}

Return only JSON.
"""
