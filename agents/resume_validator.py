class ResumeValidator:

    def validate(self, resume_data):

        report = {}

        # Summary is a string
        report["Professional Summary"] = bool(
            resume_data.get("summary", "").strip()
        )

        # These are lists
        report["Technical Skills"] = bool(
            resume_data.get("skills", [])
        )

        report["Projects"] = bool(
            resume_data.get("projects", [])
        )

        report["Education"] = bool(
            resume_data.get("education", [])
        )

        report["Certifications"] = bool(
            resume_data.get("certifications", [])
        )

        report["Experience"] = bool(
            resume_data.get("experience", [])
        )

        report["Overall Status"] = all(report.values())

        return report