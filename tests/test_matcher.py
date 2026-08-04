from agents.ats_matcher import ATSMatcher

resume = {
    "skills": ["Python", "SQL"],
    "tools": ["Git"],
    "cloud": ["Azure Databricks"],
    "frameworks": ["PySpark"]
}

jd = {
    "skills": ["Python", "SQL"],
    "tools": ["Git"],
    "cloud": ["Azure Databricks", "Azure Data Factory"],
    "frameworks": ["PySpark", "Apache Spark"]
}

matcher = ATSMatcher()

result = matcher.compare(resume, jd)

print(result)