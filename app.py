from agents.gemini_extracted_keyword import GeminiKeywordExtractor

jd = """
Working knowledge of data pipeline development using PySpark, Apache Spark, Airflow, dbt, Dagster, or equivalent technologies.
 Experience working with structured data from databases, APIs, enterprise applications, data lakes, warehouses, or lakehouse platforms.
 Exposure to cloud data platforms such as Databricks, Snowflake, BigQuery, Azure Data Lake, AWS S3, Google Cloud Storage, or equivalent platforms.
 Understanding of data modelling, schema design, joins, keys, relationships, data validation, and data quality concepts.
 Practical experience with data profiling, cleansing, transformation, and reconciliation.
 Familiarity with Git, CI/CD basics, unit testing, and production-grade engineering practices.
 Build and maintain data ingestion pipelines for structured enterprise systems such as ERP, CRM, billing, finance, HR, OSS/BSS, ServiceNow, Salesforce, SAP, Oracle, databases, and APIs.
 Build pipelines for unstructured and semi-structured data sources such as documents, emails, logs, transcripts, PDFs, spreadsheets, and media metadata.
 Develop ETL/ELT workflows using Python, SQL, PySpark, Apache Spark, Airflow, dbt, Dagster, cloud-native services, or equivalent technologies.
 Support data profiling routines to identify missing values, duplicates, inconsistent formats, incomplete master data, schema changes, and conflicting records.
 Implement data quality checks using frameworks such as Great Expectations, dbt tests, AWS Glue DataBrew, custom validation scripts, or equivalent tools.
 Support data labelling, contextualization, harmonization, enrichment, and classification workflows required for AI agent configuration.
aaaPrepare data outputs for downstream AI consumption, including embeddings, metadata, semantic tags, graph-ready datasets, and retrieval-ready document chunks.
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