from agents.resume_reader import ResumeReader
from agents.gemini_resume_extractor import GeminiResumeExtractor
from agents.gemini_extracted_keyword import GeminiKeywordExtractor
from agents.ats_matcher import ATSMatcher
from agents.resume_optimizer import ResumeOptimizer
from agents.resume_writer import ResumeWriter
from agents.resume_validator import ResumeValidator
from agents.report_generator import ReportGenerator
from agents.jd_reader import JDReader
from agents.logger import ProjectLogger
import argparse

parser = argparse.ArgumentParser(
    description="ATS Resume AI Agent"
)

parser.add_argument(
    "--resume",
    required=True,
    help="Path to the resume (.docx)"
)

parser.add_argument(
    "--jd",
    required=True,
    help="Path to the job description (.txt)"
)

args = parser.parse_args()

from agents.file_manager import FileManager
from config import (
    RESUME_PATH,
    JD_PATH,
    OUTPUT_RESUME,
    OUTPUT_REPORT
)

#CREATE LOGGER
logger = ProjectLogger()


FileManager.create_project_folders()


try:


    # READ RESUME
    

    print("Reading Resume...")
    logger.info("Reading Resume")

    reader = ResumeReader(args.resume)
    resume_text = reader.read_resume()

    print("✅ Resume Read Successfully")
    logger.info("Resume Read Successfully")


    # ANALYZE RESUME
 

    print("\nAnalyzing Resume...")
    logger.info("Analyzing Resume")

    resume_ai = GeminiResumeExtractor()
    resume_data = resume_ai.extract(resume_text)

    print("✅ Resume Analysis Completed")
    logger.info("Resume Analysis Completed")


    # VALIDATE RESUME


    print("\nValidating Resume...")
    logger.info("Validating Resume")

    validator = ResumeValidator()

    validation_report = validator.validate(resume_data)

    print("✅ Resume Validation Completed")
    logger.info("Resume Validation Completed")

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
    logger.info("Reading Job Description")

    jd_reader = JDReader(args.jd)

    jd = jd_reader.read_jd()

    print("✅ Job Description Read Successfully")
    logger.info("Job Description Read Successfully")

    # ANALYZE JOB DESCRIPTION

    print("\nAnalyzing Job Description...")
    logger.info("Analyzing Job Description")

    jd_ai = GeminiKeywordExtractor()
    jd_data = jd_ai.extract(jd)

    print("✅ Job Description Analysis Completed")
    logger.info("Job Description Analysis Completed")



    # ATS MATCHING
  

    print("\nComparing Resume with Job Description...")
    logger.info("Starting ATS Matching")

    matcher = ATSMatcher()

    ats_report = matcher.compare(
        resume_data,
        jd_data
    )

    print("✅ ATS Comparison Completed")
    logger.info("ATS Comparison Completed")


 
    # RESUME OPTIMIZATION
   

    print("\nOptimizing Resume...")
    logger.info("Resume Optimization Started")

    optimizer = ResumeOptimizer()

    optimized_resume = optimizer.optimize(
        resume_data,
        jd_data,
        ats_report
    )

    print("✅ Resume Optimized")
    logger.info("Resume Optimization Completed")


 
    # WRITE OPTIMIZED RESUME


    print("\nGenerating Optimized Resume...")
    logger.info("Generating Optimized Resume")

    
    writer = ResumeWriter(RESUME_PATH)

    writer.update_summary(
        optimized_resume["summary"]
    )

    writer.update_skills(
        optimized_resume["skills"]
    )

    writer.save(OUTPUT_RESUME)

    print("✅ Optimized Resume Generated")
    logger.info("Optimized Resume Saved")


   
    # GENERATE ATS REPORT FILE
  

    print("\nGenerating ATS Report...")
    logger.info("Generating ATS Report")

    report = ReportGenerator()

    report.generate(
        validation_report,
        ats_report,
        OUTPUT_REPORT
    )

    print("✅ ATS Report Generated")
    logger.info("ATS Report Generated Successfully")



    # DISPLAY ATS REPORT
  

    print("\n")
    print("=" * 60)
    print("                 ATS MATCH REPORT")
    print("=" * 60)

    print(f"\nATS Score : {ats_report['score']}%")
    logger.info(f"ATS Score : {ats_report['score']}%")

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
    print(f"✓ {OUTPUT_RESUME}")
    print(f"✓ {OUTPUT_REPORT}")

    logger.info("Project Completed Successfully")


except Exception as e:

    logger.error(f"Project Failed : {str(e)}")

    print("\n❌ Error Occurred")
    print(e)

    # Run this command 
    #python main.py --resume resume.docx --jd jd.txt