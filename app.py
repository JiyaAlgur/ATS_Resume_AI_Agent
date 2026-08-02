from agents.gemini_extracted_keyword import GeminiKeywordExtractor

jd = """
Working knowledge of data pipeline development using PySpark, Apache Spark, Airflow, dbt, Dagster, or equivalent technologies.
 Experience 
"""

extractor = GeminiKeywordExtractor()

result = extractor.extract(jd)

print("\n" + "=" * 60)
print("        JOB DESCRIPTION ANALYSIS")
print("=" * 60)

print(f"\nRole:")
print(result["role"])

print(f"\nExperience:")
print(result["experience"])

print(f"\nEducation:")
print(result["education"])

print(f"\nSkills:")
for skill in result["skills"]:
    print(f"  • {skill}")

print(f"\nTools:")
for tool in result["tools"]:
    print(f"  • {tool}")

print(f"\nCloud Technologies:")
for cloud in result["cloud"]:
    print(f"  • {cloud}")

print(f"\nDatabases:")
for database in result["databases"]:
    print(f"  • {database}")

print(f"\nFrameworks:")
for framework in result["frameworks"]:
    print(f"  • {framework}")

print(f"\nResponsibilities:")
if result["responsibilities"]:
    for responsibility in result["responsibilities"]:
        print(f"  • {responsibility}")
else:
    print("  • No responsibilities found")