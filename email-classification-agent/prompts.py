ZERO_SHOT_PROMPT = """
Classify the email below.

Return:
- category (spam, work, personal, promotional, support)
- priority (high, medium, low)
- sentiment (positive, neutral, negative)
- summary
- action_required (true/false)

Email:

{email}

Return only JSON.
"""


ONE_SHOT_PROMPT = """
You are an expert email classifier.

Example:

Email:
Subject: Your order has shipped!
Body: Hi, your order #1234 has been shipped and will arrive in 3 days.

Classification:
{{
  "category": "promotional",
  "priority": "low",
  "sentiment": "positive",
  "summary": "Order shipment notification",
  "action_required": false
}}

Now classify:

{email}

Return only JSON.
"""


FEW_SHOT_PROMPT = """
Example 1

Email:
Subject: Meeting at 3pm
Body: Team, please join the standup at 3pm today.

Classification:
{{"category":"work","priority":"high","sentiment":"neutral",
"summary":"Meeting reminder","action_required":true}}

---

Example 2

Email:
Subject: You won a prize!
Body: Click here to claim your $1000 reward now!!!

Classification:
{{"category":"spam","priority":"low",
"sentiment":"positive",
"summary":"Spam prize scam",
"action_required":false}}

---

Example 3

Email:
Subject: Invoice overdue
Body: Your invoice #567 is 30 days overdue. Please pay immediately.

Classification:
{{"category":"work","priority":"high","sentiment":"negative",
"summary":"Overdue invoice notice","action_required":true}}

---

Now classify:

{email}

Return only JSON.
"""


COT_PROMPT = """
You are an email classifier.

Think step by step.

Step 1: Identify the sender intent.
Step 2: Determine the category (spam, work, personal, promotional, support).
Step 3: Assess urgency and set priority (high, medium, low).
Step 4: Detect sentiment (positive, neutral, negative).
Step 5: Write a one-line summary.
Step 6: Decide if action is required.

Email:

{email}

Return only JSON.
"""


ITERATIVE_PROMPT = """
You are an email classifier.

First pass: Read the email and draft an initial classification.
Second pass: Review and refine your classification for accuracy.
Final pass: Output the final classification.

Email:

{email}

Return only JSON.
"""


NEGATIVE_PROMPT = """
You are an email classifier.

Do NOT:
- Guess information not present in the email
- Mark every email as high priority
- Classify promotional emails as spam
- Give vague summaries

Only use information present in the email.

Email:

{email}

Return only JSON.
"""


HYBRID_PROMPT = """
You are an email classifier.

Example:

Email:
Subject: Server down
Body: Production server is down. Immediate action needed.

Classification:
{{"category":"work",
"priority":"high","sentiment":"negative",
"summary":"Production server outage",
"action_required":true}}

---

Think step-by-step. Do NOT make assumptions beyond the email content.

Email:

{email}

Return only JSON.
"""


PROMPT_CHAINING_PROMPT = """
You are an email classifier.

Task 1: Extract the subject, sender intent, and key phrases.
Task 2: Assign category (spam, work, personal, promotional, support).
Task 3: Determine priority and sentiment.
Task 4: Write a one-line summary and decide if action is required.

Email:

{email}

Return only JSON.
"""

