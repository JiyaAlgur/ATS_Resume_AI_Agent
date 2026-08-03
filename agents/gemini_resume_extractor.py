import json
from google import genai
from config import GEMINI_API_KEY


class GeminiResumeExtractor:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def extract(self, resume_text):

        prompt = f"""
You are an ATS Resume Expert.

Analyze the following resume.

Extract ONLY the following information.

Return ONLY valid JSON.

{{
    "summary": "",
    "skills": [],
    "tools": [],
    "cloud": [],
    "databases": [],
    "frameworks": [],
    "projects": [],
    "experience": []
}}

Resume:

{resume_text}
"""

        response = self.client.models.generate_content(
            model="gemini-3.5-flash-lite",
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