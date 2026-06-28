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

load_dotenv()


client = Groq(
api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are a Contract Risk Analyzer specializing in contract review, legal risk identification, compliance assessment, obligation tracking, and clause analysis.

Your responsibilities:
Analyze contracts based on the text provided.
-Identify potential legal, financial, operational, and compliance risks.
- Highlight ambiguous, unfavorable, or missing clauses.
-Explain contract terms in clear and simple language.
- Assess the impact and severity of identified risks.
- Suggest mitigation strategies and negotiation points.
- Summarize key obligations, rights, deadlines, and liabilities.
Guidelines:
- Do not provide legal advice or claim to replace a licensed attorney.
- Clearly state assumptions when contract information is incomplete.
- Base all assessments solely on the contract text provided.
- Distinguish between low, medium, and high-risk findings.
- Highlight areas requiring legal review.
- Remain objective and evidence-based.
- Explain legal terminology in plain language when possible.
Output Structure:
1. Contract Overview
2. Risk Analysis
3. Key Findings
4. Recommendations
5. Action Plan
If a user asks a question outside your scope, respond with:
"Out of Scope: I am a Contract Risk Analyzer and can only assist with contract review, clause analysis, risk assessment, compliance considerations, and related contract-management topics."
"""
contract_text = """
SERVICE AGREEMENT

The Client agrees to pay the Vendor within 120 days of invoice receipt.

The Vendor shall not be liable for any indirect, incidental,
special, or consequential damages.
Either party may terminate this agreement with 7 days written notice
All intellectual property created during the project shall remain
the sole property of the Vendor.
The Vendor may increase service fees at any time without prior notice.
The Client shall indemnify and hold harmless the Vendor against all claims.
"""

all_prompts = {
"COT": COT_PROMPT
}

analysis_results = {}

for technique, prompt_template in all_prompts.items():
  
 prompt = prompt_template.replace(
    "<<CONTRACT>>",
    contract_text
)

response = client.chat.completions.create(
    model="",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.0,
    top_p=1.0,
    max_tokens=700,
    seed=50,
    response_format={"type": "json_object"},
)

output = response.choices[0].message.content

analysis_results[technique] = output

print("\n" + "=" * 60)
print(f"TECHNIQUE: {technique}")
print("=" * 60)
print(output)

