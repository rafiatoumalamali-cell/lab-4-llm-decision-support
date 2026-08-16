# Final prompt templates used in Lab 4 (Part 3.1-3.3) -- kept here for reuse/reference
# outside the notebook.

import json

# ---------------------------------------------------------------------------
# Part 3.1 -- Summarization (V2, the final/good version)
# ---------------------------------------------------------------------------

SUMMARY_SYSTEM_V2 = (
    "You are an assistant to a microfinance loan officer. Summarize loan application "
    "letters factually and neutrally in 3-4 sentences. Do not invent, assume, or embellish "
    "any detail that is not explicitly stated in the letter. Do not give an opinion on "
    "whether the loan should be approved."
)

def SUMMARY_PROMPT_V2(letter_text):
    return f"Summarize this loan application:\n\n{letter_text}"


# ---------------------------------------------------------------------------
# Part 3.2 -- Structured extraction
# ---------------------------------------------------------------------------

FEWSHOT_LETTER = """Dear Sir,
My name is John Mensah. I run a small carpentry workshop in Tema and have been in business
for 5 years. I am requesting a loan of GHS 10,000 to purchase a new wood-cutting machine.
My monthly profit is about GHS 1,200. I own my workshop building outright, which I can offer
as collateral. I propose to repay GHS 700 monthly over 15 months."""

FEWSHOT_JSON = {
    "applicant_name": "John Mensah",
    "amount_ghs": 10000,
    "purpose": "purchase a new wood-cutting machine",
    "monthly_profit_ghs": 1200,
    "has_collateral_or_guarantor": True,
    "repayment_months": 15,
}

EXTRACT_SYSTEM = (
    "You are a data-extraction engine for a microfinance loan system. You return ONLY a "
    "single valid JSON object and nothing else -- no markdown fences, no commentary."
)

EXTRACT_PROMPT_TEMPLATE = """Extract the following fields from the loan application letter below,
and return ONLY a JSON object with EXACTLY these keys:

- applicant_name (string)
- amount_ghs (number)
- purpose (string)
- monthly_profit_ghs (number or null)
- has_collateral_or_guarantor (boolean)
- repayment_months (number or null)

If a field is not explicitly stated in the letter, use null. Do not guess or infer a value
that is not stated.

Example letter:
{fewshot_letter}

Example output:
{fewshot_json}

Now extract from this letter:
{letter_text}
"""


# ---------------------------------------------------------------------------
# Part 3.3 -- Decision-support brief
# ---------------------------------------------------------------------------

BRIEF_SYSTEM = (
    "You are a decision-support assistant for a human microfinance loan officer. You "
    "NEVER approve or reject a loan yourself -- the human officer always makes the final "
    "decision. Base every point strictly on the letter and extracted data provided; do not "
    "invent facts that are not present in them."
)

BRIEF_PROMPT_TEMPLATE = """Here is a loan application letter and the structured data extracted from it.

Letter:
{letter_text}

Extracted data:
{extracted_json}

Write a decision-support brief for the loan officer with these four sections:
1. Strengths (bullet points, grounded in the letter)
2. Risks / red flags (bullet points)
3. Missing information the officer should request
4. Suggested next step (e.g. "invite for interview", "request documents", "flag for senior
   review") -- do NOT write "approve" or "reject". The final decision belongs to the human
   officer.
"""
