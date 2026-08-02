from agents.resume_writer import ResumeWriter

writer = ResumeWriter("uploads/resumes/sample_resume.docx")

writer.update_summary(
    "Data Engineer with expertise in Python, SQL, PySpark, Azure Databricks, and Delta Lake, building scalable ETL pipelines."
)

writer.update_skills([
    "Python",
    "SQL",
    "PySpark",
    "Azure Databricks",
    "Delta Lake",
    "Azure Data Factory"
])

writer.save("outputs/optimized_resume.docx")

print("Resume Updated Successfully!")