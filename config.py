import os
from dotenv import load_dotenv

load_dotenv()


# GEMINI


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

# OUTPUT FILES


OUTPUT_RESUME = "outputs/optimized_resume.docx"
OUTPUT_REPORT = "outputs/ATS_Report.txt"


# LOG FILE


LOG_FILE = "logs/project.log"