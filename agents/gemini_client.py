import time

from google import genai

from config import GEMINI_API_KEY, MODEL_NAME
from agents.exceptions import GeminiAPIError


class GeminiClient:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, prompt, retries=3):

        for attempt in range(retries):

            try:

                response = self.client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt
                )

                return response.text

            except Exception as e:

                if attempt == retries - 1:
                    raise GeminiAPIError(
                        f"Gemini API failed: {str(e)}"
                    )

                time.sleep(2)