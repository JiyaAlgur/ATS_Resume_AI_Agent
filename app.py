from agents.gemini_extracted_keyword import GeminiKeywordExtractor

jd = """
We are looking for a passionate and curious Associate Data & AI Engineer to join our Vehicle Power Management and Systems team. In this role, you will work at the intersection of automotive engineering, data analytics, and artificial intelligence to transform complex laboratory and vehicle data into meaningful engineering insights.

You will collaborate with system engineers, verification engineers, and software developers to analyze data generated from component-level testing, subsystem validation, and vehicle testing. Your work will help improve product quality, accelerate root cause analysis, enhance validation efficiency, and support the development of next-generation data-driven engineering capabilities.

This is an excellent opportunity for someone interested in applying AI and data science to solve real-world engineering challenges in the automotive industry.

Job Description

As a Data and AI Engineer, on a typical day you will

Data Engineer & Analyze

Analyze data generated from physical testing of low-voltage electrical components, including:
Batteries
Alternators
DC/DC converters
Fuse systems
Power distribution modules
Relays and electrical loads
Correlate electrical measurements such as voltage, current, power, temperature, state-of-charge etc with component behavior.
Develop automated data pipelines for ingesting and organizing test data from multiple sources.
Perform exploratory data analysis to identify trends, anomalies, and performance characteristics.
Create dashboards and visualizations that enable engineers to make informed decisions quickly.
Create automation scripts and framework to control complex lab equipment.
Analyze data collected from vehicles and Investigate field issues using recorded vehicle logs.
Correlate laboratory observations with real-world vehicle behavior.
Support root cause analysis using both laboratory and vehicle data.
Develop scripts and software tools to automate repetitive engineering tasks.
Apply ArtificiaI Intelligence & Machine Learning

To Develop models to identify patterns, detect anomalies, and predict component or system behavior.
For statistical and machine learning techniques to improve test analysis and engineering decision-making.
Explore Generative AI and intelligent assistants to improve engineering productivity and knowledge retrieval.
Continuously evaluate emerging AI technologies applicable to automotive validation and system development.

Required Qualification

Bachelor's or Master's degree in Electrical Engineering, Electronics, Data Science, Artificial Intelligence, or a related field.
1–3 years of experience in Data Engineering, AI, Machine Learning, or Analytics.
Strong Basics in automotive electrical and embedded systems.
Strong programming skills in Python.
Good understanding of SQL and data manipulation.
Knowledge of statistics and data analysis techniques.
Familiarity with machine learning fundamentals.
Good problem-solving and analytical skills.
Strong communication and collaboration abilities.

Preferred Qualification

Understanding of vehicle communication protocols such as CAN,LIN etc.
Familiarity with automotive data formats and logging tools.
Experience using visualization tools such as Power BI, Tableau, or Plotly.
Exposure to cloud data platforms or big data technologies.
Basic understanding of signal processing.

What You'll Learn

Automotive electrical architecture and low-voltage power management systems.
Hands-on experience with laboratory validation using real hardware.
Analysis of real vehicle data collected during development and validation.
AI applications in automotive engineering.
Data-driven verification and validation methodologies.
Cross-functional collaboration within a global engineering organization.

We value your data privacy and therefore do not accept applications via mail.

Who We Are And What We Believe In

We are committed to shaping the future landscape of efficient, safe, and sustainable transport solutions. Fulfilling our mission creates countless career opportunities for talents across the group’s leading brands and entities.

Applying to this job offers you the opportunity to join Volvo Group. Every day, you will be working with some of the sharpest and most creative brains in our field to be able to leave our society in better shape for the next generation. We are passionate about what we do, and we thrive on teamwork. We are almost 100,000 people united around the world by a culture of care, inclusiveness, and empowerment.

Trucks Technology & Industrial Division hire team players who are ready to create real customer impact. Our decentralized teams work close to our customers, with speed and autonomy, to build what they truly need.

Join us to collaborate on innovative, sustainable technologies that redefine how we design, build, and deliver value. Bring your curiosity, your expertise, and your collaborative energy, and together, we’ll turn bold ideas into tangible solutions for our customers and contribute to a more sustainable tomorrow.
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