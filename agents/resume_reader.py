from docx import Document


class ResumeReader:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_resume(self):
        document = Document(self.file_path)

        text = []

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                text.append(paragraph.text)

        return "\n".join(text)