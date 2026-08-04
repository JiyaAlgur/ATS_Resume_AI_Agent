# ATS Resume AI Agent

## Overview

ATS Resume AI Agent is an AI-powered resume optimization tool that analyzes a candidate's resume against a job description and generates an ATS-friendly optimized resume. The application leverages Google's Gemini API to extract structured information, compare skills, identify missing keywords, and improve resume quality while preserving the candidate's genuine experience.

This project was built using Python with a modular architecture, making it easy to maintain, extend, and reuse.

---

## Features

* Read resumes from Microsoft Word (.docx) files.
* Read job descriptions from text (.txt) files.
* Extract structured resume information using Gemini AI.
* Extract skills, tools, cloud technologies, and responsibilities from job descriptions.
* Compare resumes against job descriptions.
* Calculate an ATS match score.
* Identify matched, missing, and additional skills.
* Validate essential resume sections.
* Optimize the Professional Summary and Technical Skills.
* Generate an optimized resume in DOCX format.
* Generate ATS reports in TXT and PDF formats.
* Log application execution for debugging and monitoring.
* Handle API errors, invalid JSON, and runtime exceptions gracefully.
* Run using Command Line Interface (CLI) arguments.

---

## Tech Stack

### Programming Language

* Python

### AI

* Google Gemini API

### Libraries

* python-docx
* reportlab
* python-dotenv
* argparse

### Concepts Used

* Object-Oriented Programming (OOP)
* Modular Architecture
* Exception Handling
* Logging
* JSON Processing
* ATS Resume Optimization
* Prompt Engineering

---

## Project Structure

```text
ATS_Resume_AI_Agent/
│
├── agents/
│   ├── ats_matcher.py
│   ├── exceptions.py
│   ├── gemini_client.py
│   ├── gemini_extracted_keyword.py
│   ├── gemini_resume_extractor.py
│   ├── jd_reader.py
│   ├── logger.py
│   ├── report_generator.py
│   ├── resume_optimizer.py
│   ├── resume_reader.py
│   ├── resume_validator.py
│   ├── resume_writer.py
│   └── skill_normalizer.py
│
├── uploads/
│   ├── resumes/
│   └── job_descriptions/
│
├── outputs/
│
├── logs/
│
├── main.py
├── config.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/ATS_Resume_AI_Agent.git
```

Move into the project directory:

```bash
cd ATS_Resume_AI_Agent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```text
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
MODEL_NAME=gemini-2.5-flash
```

---

## Usage

Place your files in the following folders:

```text
uploads/
├── resumes/
│   └── sample_resume.docx
└── job_descriptions/
    └── sample_jd.txt
```

Run the application:

```bash
python main.py --resume uploads/resumes/sample_resume.docx --jd uploads/job_descriptions/sample_jd.txt
```

---

## Generated Outputs

After execution, the application generates:

```text
outputs/
├── optimized_resume.docx
├── ATS_Report.txt
└── ATS_Report.pdf
```

---

## Sample Console Output

```text
Reading Resume...
Resume Read Successfully

Analyzing Resume...
Resume Analysis Completed

Reading Job Description...
Job Description Read Successfully

Analyzing Job Description...
Job Description Analysis Completed

Comparing Resume with Job Description...
ATS Comparison Completed

Optimizing Resume...
Resume Optimized

Generating Optimized Resume...
Optimized Resume Generated

Generating ATS Report...
ATS Report Generated
```

---

## Error Handling

The application handles common failure scenarios, including:

* Invalid Gemini API Key
* Gemini API quota exceeded
* Gemini server unavailable
* Invalid JSON response from Gemini
* Missing resume file
* Missing job description file
* Unexpected runtime exceptions

---

## Future Improvements

* Resume keyword highlighting
* Support for PDF resumes
* Streamlit web interface
* Batch resume processing
* Resume ranking for multiple candidates
* HTML report generation
* ATS score visualization dashboard
* Multi-language resume support

---

## Author

**Jiya Algur**

Aspiring Data Engineer with hands-on experience in Python, SQL, PySpark, Azure Databricks, ETL pipeline development, and AI-powered automation projects.

---

## License

This project is intended for educational and portfolio purposes.
