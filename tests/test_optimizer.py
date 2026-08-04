from agents.resume_optimizer import ResumeOptimizer


# Sample Resume Data


resume_data = {
    "summary": "Data Engineer with Python and SQL.",
    "skills": [
        "Python",
        "SQL",
        "PySpark"
    ],
    "projects": [
        {
            "name": "Retail ETL",
            "description": "Built ETL pipelines."
        }
    ]
}


# Sample JD Data


jd_data = {
    "skills": [
        "Python",
        "SQL",
        "PySpark",
        "Azure Databricks",
        "Delta Lake"
    ]
}


# Sample ATS Report


ats_report = {
    "score": 72,
    "matched": [
        "Python",
        "SQL",
        "PySpark"
    ],
    "missing": [
        "Azure Databricks",
        "Delta Lake"
    ]
}

# Optimize Resume


optimizer = ResumeOptimizer()

result = optimizer.optimize(
    resume_data,
    jd_data,
    ats_report
)


# Display Report

print("\n" + "=" * 60)
print("            RESUME OPTIMIZATION REPORT")
print("=" * 60)

print("\nSUMMARY")
print("-" * 60)

print("\nBefore:")
print(resume_data["summary"])

print("\nAfter:")
print(result["summary"])

print("\nSKILLS")
print("-" * 60)

print("\nBefore:")
for skill in resume_data["skills"]:
    print(f"• {skill}")

print("\nAfter:")
for skill in result["skills"]:
    print(f"✓ {skill}")



print("\n" + "=" * 60)
print("       RESUME OPTIMIZATION COMPLETED")
print("=" * 60)