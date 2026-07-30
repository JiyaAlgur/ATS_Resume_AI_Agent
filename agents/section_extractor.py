class SectionExtractor:

    def __init__(self):

        self.headings = [
            "PROFESSIONAL SUMMARY",
            "TECHNICAL SKILLS",
            "PROFESSIONAL EXPERIENCE",
            "PROJECTS",
            "EDUCATION",
            "CERTIFICATIONS"
        ]

    def extract_sections(self, resume_text):

        sections = {}

        current_section = "HEADER"
        sections[current_section] = []

        lines = resume_text.split("\n")

        for line in lines:

            line = line.strip()

            if not line:
                continue

            if line.upper() in self.headings:

                current_section = line.upper()

                sections[current_section] = []

            else:

                sections[current_section].append(line)

        return sections