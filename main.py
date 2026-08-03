from agents.resume_reader import ResumeReader
from agents.gemini_resume_extractor import GeminiResumeExtractor
from agents.gemini_extracted_keyword import GeminiKeywordExtractor
from agents.ats_matcher import ATSMatcher
from agents.resume_optimizer import ResumeOptimizer
from agents.resume_writer import ResumeWriter
from agents.resume_validator import ResumeValidator
from agents.report_generator import ReportGenerator
from agents.jd_reader import JDReader



# READ RESUME


print("Reading Resume...")

reader = ResumeReader("uploads/resumes/sample_resume.docx")
resume_text = reader.read_resume()

print("✅ Resume Read Successfully")



# ANALYZE RESUME


print("\nAnalyzing Resume...")

resume_ai = GeminiResumeExtractor()
resume_data = resume_ai.extract(resume_text)

print("✅ Resume Analysis Completed")



# VALIDATE RESUME


print("\nValidating Resume...")

validator = ResumeValidator()

validation_report = validator.validate(resume_data)

print("✅ Resume Validation Completed")

print("\n" + "=" * 60)
print("             RESUME VALIDATION REPORT")
print("=" * 60)

for section, status in validation_report.items():

    if section == "Overall Status":
        continue

    icon = "✓" if status else "✗"

    print(f"{icon} {section}")

print("\nOverall Status:")

if validation_report["Overall Status"]:
    print("✓ Resume Structure Valid")
else:
    print("✗ Resume Structure Incomplete")

print("=" * 60)





# READ JOB DESCRIPTION


print("\nReading Job Description...")

jd_reader = JDReader(
    "uploads/job_descriptions/sample_jd.txt"
)

jd = jd_reader.read_jd()

print("✅ Job Description Read Successfully")



# ANALYZE JOB DESCRIPTION


print("\nAnalyzing Job Description...")

jd_ai = GeminiKeywordExtractor()
jd_data = jd_ai.extract(jd)

print("✅ Job Description Analysis Completed")



# ATS MATCHING


print("\nComparing Resume with Job Description...")

matcher = ATSMatcher()

ats_report = matcher.compare(
    resume_data,
    jd_data
)

print("✅ ATS Comparison Completed")



# RESUME OPTIMIZATION


print("\nOptimizing Resume...")

optimizer = ResumeOptimizer()

optimized_resume = optimizer.optimize(
    resume_data,
    jd_data,
    ats_report
)

print("✅ Resume Optimized")



# WRITE OPTIMIZED RESUME


print("\nGenerating Optimized Resume...")

writer = ResumeWriter("uploads/resumes/sample_resume.docx")

writer.update_summary(
    optimized_resume["summary"]
)

writer.update_skills(
    optimized_resume["skills"]
)

writer.save("outputs/optimized_resume.docx")

print("✅ Optimized Resume Generated")



# GENERATE ATS REPORT FILE


print("\nGenerating ATS Report...")

report = ReportGenerator()

report.generate(
    validation_report,
    ats_report,
    "outputs/ATS_Report.txt"
)

print("✅ ATS Report Generated")



# DISPLAY ATS REPORT


print("\n")
print("=" * 60)
print("                 ATS MATCH REPORT")
print("=" * 60)

print(f"\nATS Score : {ats_report['score']}%")

print("\nMatched Skills")
print("-" * 30)

for skill in ats_report["matched"]:
    print(f"✓ {skill}")

print("\nMissing Skills")
print("-" * 30)

for skill in ats_report["missing"]:
    print(f"✗ {skill}")

print("\nAdditional Skills Found in Resume")
print("-" * 30)

for skill in ats_report["extra"]:
    print(f"• {skill}")


print("\n")
print("=" * 60)
print("      RESUME OPTIMIZATION COMPLETED")
print("=" * 60)

print("\nFiles Generated Successfully")
print("✓ outputs/optimized_resume.docx")
print("✓ outputs/ATS_Report.txt")