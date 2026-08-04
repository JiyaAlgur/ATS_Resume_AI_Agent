import json

from agents.gemini_client import GeminiClient
from agents.exceptions import InvalidJSONError


class GeminiResumeExtractor:

    def __init__(self):
        self.client = GeminiClient()

    def extract(self, resume_text):

        prompt = f"""
You are an ATS Resume Expert.

Analyze the following resume.

Return ONLY valid JSON.

{{
    "summary": "",
    "skills": [],
    "tools": [],
    "cloud": [],
    "databases": [],
    "frameworks": [],
    "projects": [],
    "experience": [],
    "education": [],
    "certifications": []
}}

Resume:

{resume_text}
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
                "Gemini returned invalid JSON while analyzing the resume."
            )