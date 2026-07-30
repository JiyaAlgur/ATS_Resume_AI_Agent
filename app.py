from agents.resume_reader import ResumeReader


resume = ResumeReader("uploads/resumes/sample_resume.docx")

content = resume.read_resume()

print(content)