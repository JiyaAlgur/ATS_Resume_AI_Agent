import os


class FileManager:

    @staticmethod
    def create_project_folders():

        folders = [
            "logs",
            "outputs",
            "uploads",
            "uploads/resumes",
            "uploads/job_descriptions"
        ]

        for folder in folders:
            os.makedirs(folder, exist_ok=True)