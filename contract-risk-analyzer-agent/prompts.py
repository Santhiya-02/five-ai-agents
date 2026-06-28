# prompts.py

ZERO_SHOT_PROMPT = """
Analyze the contract below.

Return:

* overall_risk_level (low, medium, high, critical)
* risks (list)
* missing_clauses (list)
* financial_liabilities (list)
* compliance_concerns (list)
* recommendations (list)
* score (0-100, higher is safer)

Contract:

<<CONTRACT>>

Return only JSON.
"""

ONE_SHOT_PROMPT = """
You are an expert legal contract analyst.

Example:

Contract:
Vendor must deliver software within 30 days.
Client pays 100% upfront.
No refund policy exists.

Analysis:
{
"overall_risk_level":"high",
"risks":[
"Upfront payment risk",
"No refund policy"
],
"missing_clauses":[
"Refund clause",
"Dispute resolution clause"
],
"financial_liabilities":[
"Loss of upfront payment"
],
"compliance_concerns":[
"No governing law clause"
],
"recommendations":[
"Add refund clause",
"Use milestone payments"
],
"score":40
}

Now analyze:

<<CONTRACT>>

Return only JSON.
"""

FEW_SHOT_PROMPT = """
Example 1

Contract:
SaaS agreement auto-renews annually.
No cancellation clause.
No GDPR language.

Analysis:
{
"overall_risk_level":"high",
"risks":[
"Unexpected renewals",
"GDPR compliance risk"
],
"missing_clauses":[
"Cancellation clause",
"Data protection clause"
],
"financial_liabilities":[
"Unexpected renewal fees"
],
"compliance_concerns":[
"GDPR risk"
],
"recommendations":[
"Add cancellation clause",
"Add GDPR clause"
],
"score":35
}

---

Example 2

Contract:
Vendor agreement includes SLA, penalties, arbitration, and GDPR terms.

Analysis:
{
"overall_risk_level":"low",
"risks":[
"Minor SLA ambiguity"
],
"missing_clauses":[
"Force majeure clause"
],
"financial_liabilities":[
"Limited financial exposure"
],
"compliance_concerns":[
"None"
],
"recommendations":[
"Add force majeure clause"
],
"score":85
}

---

Example 3

Contract:
Employment agreement contains a broad non-compete.
No IP assignment clause.

Analysis:
{
"overall_risk_level":"medium",
"risks":[
"Broad non-compete",
"Unclear IP ownership"
],
"missing_clauses":[
"IP assignment clause"
],
"financial_liabilities":[
"Potential legal disputes"
],
"compliance_concerns":[
"Non-compete enforceability"
],
"recommendations":[
"Limit non-compete scope",
"Add IP assignment clause"
],
"score":60
}

---

Now analyze:

<<CONTRACT>>

Return only JSON.
"""

COT_PROMPT = """
You are a legal contract analyst.

Think step by step.

Step 1: Identify parties and obligations.
Step 2: Identify legal risks.
Step 3: Identify operational risks.
Step 4: Identify financial liabilities.
Step 5: Identify missing clauses.
Step 6: Review compliance concerns.
Step 7: Generate recommendations.
Step 8: Assign risk level and score.

Contract:

<<CONTRACT>>

Return only JSON.
"""

ITERATIVE_PROMPT = """
You are a legal contract analyst.

First pass:
Create an initial risk assessment.

Second pass:
Review every clause carefully and identify missed risks.

Third pass:
Refine findings and produce the final contract analysis.

Contract:

<<CONTRACT>>

Return only JSON.
"""

NEGATIVE_PROMPT = """
You are a legal contract analyst.

Do NOT:

* Assume clauses exist when not mentioned
* Hallucinate risks not supported by the contract
* Give generic legal advice
* Mark every contract as high risk
* Ignore financial exposure
* Ignore compliance concerns

Only analyze information present or clearly absent in the contract.

Contract:

<<CONTRACT>>

Return only JSON.
"""

HYBRID_PROMPT = """
You are a legal contract analyst.

Example:

Contract:
Freelancer agreement.
No IP assignment clause.
Client may terminate anytime.
No compensation on termination.

Analysis:
{
"overall_risk_level":"high",
"risks":[
"Unclear IP ownership",
"Termination without compensation"
],
"missing_clauses":[
"IP assignment clause",
"Termination compensation clause"
],
"financial_liabilities":[
"Loss of unpaid work",
"IP ownership disputes"
],
"compliance_concerns":[
"Ownership ambiguity"
],
"recommendations":[
"Add IP assignment clause",
"Define termination compensation"
],
"score":35
}

Think step by step.

Do NOT assume clauses exist.

Contract:

<<CONTRACT>>

Return only JSON.
"""

PROMPT_CHAINING_PROMPT = """
You are a legal contract analyst.

Task 1: Extract parties and obligations.
Task 2: Identify risks.
Task 3: Identify missing clauses.
Task 4: Assess financial liabilities.
Task 5: Review compliance concerns.
Task 6: Generate recommendations.
Task 7: Assign overall risk level.
Task 8: Assign safety score.

Contract:

<<CONTRACT>>

Return only JSON.
"""
