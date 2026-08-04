import json

from agents.gemini_client import GeminiClient
from agents.exceptions import InvalidJSONError


class GeminiKeywordExtractor:

    def __init__(self):
        self.client = GeminiClient()

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

        text = self.client.generate(prompt)

        text = text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "", 1)

        if text.startswith("```"):
            text = text.replace("```", "", 1)

        if text.endswith("```"):
            text = text[:-3]

        text = text.strip()

        try:
            return json.loads(text)

        except json.JSONDecodeError:
            raise InvalidJSONError(
                "Gemini returned invalid JSON while analyzing the Job Description."
            )