import re

def parse_llm_output(text):
    result = {}

    # Extract score
    score_match = re.search(r'(\d{1,3})/100', text)
    result["score"] = int(score_match.group(1)) if score_match else None

    # Extract sections
    def extract_section(title):
        pattern = rf"\*\*{title}:\*\*\n(.*?)(\n\n|\Z)"
        match = re.search(pattern, text, re.DOTALL)
        return match.group(1).strip() if match else ""

    result["strengths"] = extract_section("Strengths")
    result["missing_skills"] = extract_section("Missing Skills")
    result["suggestions"] = extract_section("Suggestions")

    return result