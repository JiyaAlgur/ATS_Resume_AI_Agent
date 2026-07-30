import json
from google import genai
from config import GEMINI_API_KEY


class GeminiKeywordExtractor:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def extract(self, job_description):

        prompt = f"""
You are an ATS Resume Expert.

Analyze the following Job Description.

Extract ONLY the following information.

Return ONLY valid JSON.

{{
    "role": "",
    "experience": "",
    "education": "",
    "skills": [],
    "tools": [],
    "cloud": [],
    "databases": [],
    "frameworks": [],
    "responsibilities": []
}}

Job Description:

{job_description}
"""

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