from docx import Document

from agents.exceptions import FileReadError


class ResumeReader:

    def __init__(self, resume_path):
        self.resume_path = resume_path

    def read_resume(self):

        try:

            document = Document(self.resume_path)

            text = []

            for paragraph in document.paragraphs:
                text.append(paragraph.text)

            return "\n".join(text)

        except Exception as e:
            raise FileReadError(
                f"Unable to read resume: {e}"
            )