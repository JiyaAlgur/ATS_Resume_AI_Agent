from agents.resume_reader import ResumeReader
from agents.gemini_resume_extractor import GeminiResumeExtractor

reader = ResumeReader("uploads/resumes/sample_resume.docx")

resume_text = reader.read_resume()

extractor = GeminiResumeExtractor()

result = extractor.extract(resume_text)

print(result)