from agents.resume_reader import ResumeReader
from agents.section_extractor import SectionExtractor


reader = ResumeReader("uploads/resumes/sample_resume.docx")

resume_text = reader.read_resume()

extractor = SectionExtractor()

sections = extractor.extract_sections(resume_text)

print("\n========== RESUME SECTIONS ==========\n")

for heading, content in sections.items():

    print("=" * 70)
    print(heading)
    print("=" * 70)

    for line in content:
        print(line)

    print()