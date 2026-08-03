class JDReader:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_jd(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.read().strip()