import json
import time
from google import genai

from config import GEMINI_API_KEY


class ResumeOptimizer:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def optimize(self, resume_data, jd_data, ats_report):

        prompt = f"""
You are an ATS Resume Optimization Expert.

You will receive:

1. Resume Data
2. Job Description Data
3. ATS Match Report

Your task is to improve ONLY the following sections:

1. Professional Summary
2. Technical Skills

STRICT RULES

1. DO NOT modify Professional Experience.
2. DO NOT modify Projects.
3. DO NOT modify Education.
4. DO NOT modify Certifications.
5. DO NOT invent fake experience.
6. DO NOT invent companies or job titles.
7. Include important ATS keywords from the Job Description ONLY if they are relevant to the candidate's existing background.
8. Add missing technical skills only if they naturally fit the candidate's profile.
9. Keep the summary concise (2–3 lines), ATS-friendly, and professional.
10. Return ONLY valid JSON.

Output Format:

{{
    "summary": "",
    "skills": []
}}

Resume Data:
{json.dumps(resume_data, indent=2)}

Job Description:
{json.dumps(jd_data, indent=2)}

ATS Report:
{json.dumps(ats_report, indent=2)}
"""

        max_retries = 3

        for attempt in range(max_retries):

            try:

                response = self.client.models.generate_content(
                    model="gemini-flash-latest",
                    contents=prompt
                )

                text = response.text.strip()

                if text.startswith("```json"):
                    text = text.replace("```json", "", 1)

                if text.startswith("```"):
                    text = text.replace("```", "", 1)

                if text.endswith("```"):
                    text = text[:-3]

                text = text.strip()

                return json.loads(text)

            except Exception as e:

                print(f"\n⚠ Gemini API Error (Attempt {attempt + 1}/{max_retries})")
                print(e)

                if attempt < max_retries - 1:
                    print("Retrying in 5 seconds...\n")
                    time.sleep(5)
                else:
                    print("\n❌ Unable to optimize resume.")
                    print("Returning original summary and skills.\n")

                    return {
                        "summary": resume_data["summary"],
                        "skills": resume_data["skills"]
                    }