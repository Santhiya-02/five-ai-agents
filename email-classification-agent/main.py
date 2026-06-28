import os
from groq import Groq
from dotenv import load_dotenv
from prompts import (
    ZERO_SHOT_PROMPT,
    ONE_SHOT_PROMPT,
    FEW_SHOT_PROMPT,
    COT_PROMPT,
    ITERATIVE_PROMPT,
    NEGATIVE_PROMPT,
    HYBRID_PROMPT,
    PROMPT_CHAINING_PROMPT,
)

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
SYSTEM_PROMPT = """
You are an Email Classification Agent that analyzes emails and classifies them into predefined categories.
Your tasks:
- Read the email content.
- Identify the email category.
- Determine the sender's intent.
- Assess the priority level.
- Extract key action items if present.
- Detect spam, phishing, or suspicious content.
-reasoning
Categories:
Work, Personal, Support, Sales/Marketing, Finance, HR, Meeting/Scheduling, Notification, Spam, Phishing, Other.
For every email, return:
Category: <category>
Intent: <intent>
Priority: <Low/Medium/High>
Summary: <1-2 sentence summary>
Action Items: <list or None>
Security Status: <Safe/Spam/Phishing>
Rules:
- Base your analysis only on the email content provided.
- Do not invent information.
- Keep responses concise and structured.
- If the email appears malicious, clearly explain why.
- If the category is uncertain, choose the closest match and state the uncertainty.
If the input is not an email, respond with:
"Out of Scope: Please provide an email for classification."
"""
email = """
Subject: Meeting Reminder
Hi Team,
Reminder: Project review meeting tomorrow at 10 AM in Conference Room A.
Thanks,
Manager
"""

PROMPTS = {
    "ONE_SHOT": ONE_SHOT_PROMPT,
    
}

for technique, prompt_template in PROMPTS.items():

    print("\n" + "=" * 60)
    print(f"TECHNIQUE: {technique}")
    print("=" * 60)

    prompt = prompt_template.format(email=email)

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.0,
            max_tokens=600,
            response_format={"type": "json_object"},
            seed=50,
            top_p=0.6
        )

        print(response.choices[0].message.content)

    except Exception as e:
        print(f"Error: {e}")