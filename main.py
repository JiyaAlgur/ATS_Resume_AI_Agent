from agents.resume_reader import ResumeReader
from agents.gemini_resume_extractor import GeminiResumeExtractor
from agents.gemini_extracted_keyword import GeminiKeywordExtractor
from agents.ats_matcher import ATSMatcher



#READ RESUME


print("Reading Resume...")

reader = ResumeReader("uploads/resumes/sample_resume.docx")
resume_text = reader.read_resume()

print("✅ Resume Read Successfully")



#ANALYZE RESUME USING GEMINI


print("\nAnalyzing Resume...")

resume_ai = GeminiResumeExtractor()
resume_data = resume_ai.extract(resume_text)

print("✅ Resume Analysis Completed")



#JOB DESCRIPTION


jd = """
Qualifications

A bachelor’s degree in Computer Science or related field with 6-12 years of technology experience

Strong experience in System Integration, Application Development or Data-Warehouse projects, across technologies used in the enterprise space

Software development experience using: Object-oriented languages (e.g. Python, PySpark,) and frameworks

Database programming using any flavors of SQL

Expertise in relational and dimensional modelling, including big data technologies

Exposure across all the SDLC process, including testing and deployment

Expertise in Microsoft Azure is mandatory including components like Azure Data Factory, Azure Data Lake Storage, Azure SQL, Azure Databricks, HD Insights, ML Service etc.

Good knowledge of Python and Spark are required

Good understanding of how to enable analytics using cloud technology and ML Ops

Experience in Azure Infrastructure and Azure Dev Ops will be a strong plus

Proven track record in keeping existing technical skills and developing new ones

Characteristics of a forward thinker and self-starter

Ability to work with a global team of consulting professionals across multiple projects

Passion for educating, training, designing, and building end-to-end systems

GenAI - added advantage
"""


#ANALYZE JOB DESCRIPTION


print("\nAnalyzing Job Description...")

jd_ai = GeminiKeywordExtractor()
jd_data = jd_ai.extract(jd)

print("✅ Job Description Analysis Completed")



#ATS MATCHING


print("\nComparing Resume with Job Description...")

matcher = ATSMatcher()

result = matcher.compare(
    resume_data,
    jd_data
)

print("✅ ATS Comparison Completed")



#DISPLAY REPORT

print("\n")
print("=" * 60)
print("                 ATS MATCH REPORT")
print("=" * 60)

print(f"\nATS Score : {result['score']}%")

print("\nMatched Skills")
print("-" * 30)

for skill in result["matched"]:
    print(f"✓ {skill}")

print("\nMissing Skills")
print("-" * 30)

for skill in result["missing"]:
    print(f"✗ {skill}")

print("\nAdditional Skills Found in Resume")
print("-" * 30)

for skill in result["extra"]:
    print(f"• {skill}")

print("\n")
print("=" * 60)
print("           ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)